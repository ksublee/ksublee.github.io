"""Refresh generated publication lists and the offline preview before Quarto renders."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).resolve().parent
PAGES = ("index", "research", "teaching", "software", "cv")


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


def write(name, text):
    path = ROOT / name
    if not path.exists() or read(name) != text:
        path.write_text(text, encoding="utf-8", newline="\n")


def coauthors(names):
    if len(names) < 2:
        return "".join(names)
    if len(names) == 2:
        return " and ".join(names)
    return ", ".join(names[:-1]) + ", and " + names[-1]


def articles(papers, working=False):
    result = []
    for paper in papers:
        url = escape(paper["url"], quote=True)
        parts = [f'<article class="pub"><div class="year">{paper["year"]}</div><div>',
                 f'<h3><a href="{url}">{escape(paper["title"])}</a></h3>']
        if paper.get("coauthors"):
            parts.append(f'<p class="coauthors">with {escape(coauthors(paper["coauthors"]))}</p>')
        parts.append('<p>Working paper</p>' if working else f'<p>{escape(paper["journal"])}</p>')
        label = "arXiv" if working else "Article"
        parts.append(f'<a class="paperlink" href="{url}">{label} ↗</a>')
        if not working and paper.get("arxiv"):
            parts.append(f'<span aria-hidden="true"> · </span> <a class="paperlink" href="{escape(paper["arxiv"], quote=True)}">arXiv ↗</a>')
        parts.append('</div></article>')
        result.append("\n".join(parts))
    return "\n".join(result)


def replace_block(text, name, content):
    start, end = f'<!-- generated:{name}:start -->', f'<!-- generated:{name}:end -->'
    pattern = re.escape(start) + r'.*?' + re.escape(end)
    text, count = re.subn(pattern, lambda _: start + '\n' + content + '\n' + end, text, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected one generated block: {name}")
    return text


def main():
    papers = sorted(json.loads(read("publications.json")), key=lambda p: -p["year"])
    working = sorted(json.loads(read("working-papers.json")), key=lambda p: -p["year"])
    blocks = {
        "index": {"recent": articles(papers[:3]), "working": articles(working, True)},
        "research": {"journal": articles(papers), "working": articles(working, True)},
        "cv": {"journal": articles(papers), "working": articles(working, True)},
    }
    sources = {}
    for page in PAGES:
        text = read(page + ".qmd")
        for name, content in blocks.get(page, {}).items():
            text = replace_block(text, name, content)
        if page == "teaching":
            def sort_courses(match):
                courses = re.findall(r'<li>.*?</li>', match[1], re.S)
                courses.sort(key=lambda item: re.sub(r'<[^>]+>', '', item).casefold())
                return '<ul class="course-list">\n' + '\n'.join(courses) + '\n</ul>'
            text = re.sub(r'<ul class="course-list">(.*?)</ul>', sort_courses, text, flags=re.S)
        write(page + ".qmd", text)
        sources[page] = re.search(r'```\{=html\}\s*(.*?)\s*```', text, re.S)[1]

    home = sources["index"]
    header = home.split('<main ', 1)[0]
    footer = home.split('</main>', 1)[1]
    # Every local page link uses the same hash routing in the offline preview.
    def local_links(text):
        return re.sub(r'href="(index|research|teaching|software|cv)\.html"', r'href="#\1"', text)
    panels = []
    descriptions = {}
    for page in PAGES:
        content = re.search(r'<main\b[^>]*>(.*?)</main>', sources[page], re.S)[1]
        hidden = '' if page == 'index' else ' hidden'
        panels.append(f'<div class="preview-panel" id="panel-{page}"{hidden}>\n{local_links(content)}\n</div>')
        descriptions[page] = json.loads(re.search(r'^description: (.+)$', read(page + '.qmd'), re.M)[1])
    script = '''
const pages = new Set(['index', 'research', 'teaching', 'software', 'cv']);
const descriptions = DESCRIPTIONS;
function show(focus = false) {
  const requested = location.hash.slice(1) || 'index';
  if (!pages.has(requested)) return;
  document.querySelectorAll('.preview-panel').forEach(panel => {
    panel.hidden = panel.id !== 'panel-' + requested;
  });
  document.querySelectorAll('.navlinks a').forEach(link => {
    if (link.hash === '#' + requested) link.setAttribute('aria-current', 'page');
    else link.removeAttribute('aria-current');
  });
  const title = requested === 'index' ? 'Home' : requested === 'cv' ? 'CV' : requested[0].toUpperCase() + requested.slice(1);
  document.title = title + ' – Kyungsub Lee';
  document.querySelector('meta[name="description"]').content = descriptions[requested];
  if (focus) document.getElementById('main-content').focus({preventScroll: true});
  window.scrollTo(0, 0);
}
window.addEventListener('hashchange', () => show(true));
document.querySelector('.skip').addEventListener('click', event => {
  event.preventDefault();
  const main = document.getElementById('main-content');
  main.focus({preventScroll: true});
  main.scrollIntoView();
});
show();
'''.replace('DESCRIPTIONS', json.dumps(descriptions, ensure_ascii=False))
    preview = ('<!doctype html>\n<html lang="en"><head>\n<meta charset="utf-8">\n'
               '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
               f'<meta name="description" content="{escape(descriptions["index"], quote=True)}">\n'
               '<title>Home – Kyungsub Lee</title>\n<style>\n' + read('styles.css') + '\n</style>\n</head><body>\n'
               + local_links(header) + '<main class="main" id="main-content" tabindex="-1">\n'
               + '\n'.join(panels) + '\n</main>\n' + local_links(footer)
               + '\n<script>\n' + script + '\n</script>\n</body></html>\n')
    write('preview.html', preview)
    print(f'Updated pages and preview: {len(papers)} journal articles, {len(working)} working papers.')


if __name__ == '__main__':
    main()
