# Kyungsub Lee — academic homepage draft

## 수정과 빌드
- 소개·경력·과목: 해당 `.qmd` 파일을 수정합니다. 연구 철학 문장은 원문 그대로 유지합니다.
- 논문: `publications.json`, working papers: `working-papers.json`을 수정합니다.
- 디자인: `styles.css`를 수정합니다.
- `generated` 주석 사이의 논문 목록은 자동 생성되므로 직접 수정하지 않습니다.
- 과목은 학부·대학원별 영문명 알파벳순으로 정렬됩니다.

Python 3와 Quarto가 설치된 환경에서 `quarto render`를 실행합니다. 사전 빌드 단계에서 `build.py`가 논문 목록과 `preview.html`을 갱신합니다. 실제 배포용 HTML은 `docs/`에 생성됩니다.

오프라인 미리보기만 갱신하려면 `python build.py`를 실행한 뒤 `preview.html`을 엽니다. 미리보기는 JavaScript가 필요합니다. 배포본은 JavaScript 없이도 페이지를 읽고 이동할 수 있습니다.

2026-10-08에 Quarto 1.9.38로 5개 페이지를 렌더했습니다.

## GitHub Pages
저장소는 `ksublee/ksublee.github.io`를 사용합니다. 기본 브랜치는 `main`, Pages 배포 위치는 `main`의 `/docs`로 설정합니다. 홈페이지 주소는 https://ksublee.github.io 입니다.

수정 후 `quarto render`로 배포용 HTML을 갱신하고, 원본과 `docs/`를 함께 커밋·push합니다. `.nojekyll`은 Quarto가 만든 HTML을 그대로 배포하도록 지정합니다. `.quarto/`와 ZIP 묶음은 Git에서 제외합니다.

## 공개 전 확인 사항
1. 교수 직함 및 경력: 사용자 확인에 따라 Professor는 September 2026 – present, Associate Professor는 September 2021 – August 2026으로 반영했습니다.
2. 연구 철학 문장은 사용자 요청에 따라 원문을 유지합니다. 나머지 소개는 축약했습니다.
3. /Work/Lecture의 2015–2026년 연도·학기별 폴더명을 대조해 과목을 보완했습니다. 과목명이 같은 폴더는 통합했고 동영상·자료 보관용 폴더와 Archive는 포함하지 않았습니다. 기존 홈페이지의 확률과정은 유지했습니다. 사용자 지정에 따라 학부 12개와 대학원 8개로 구분하고 대학생활설계·취업설계는 제외했습니다. 영어 과목명은 공식 학사 영문명을 별도 확인하지 않은 번역이며, 통계적기계학습과 통계머신러닝은 서로 다른 폴더명에 따라 구분했습니다.
4. CV: 경력·학력·연구 관심 분야와 논문 22편, working paper 3편을 포함합니다. 인쇄 기능으로 PDF를 저장합니다.
5. 논문 저자명/권·호·쪽수 추가 여부. 초안은 제목·학술지·연도·DOI 중심으로 통일했습니다.

## 자료 출처와 갱신
- 기존 홈페이지: https://sites.google.com/view/ksublee
- ORCID: https://orcid.org/0000-0001-9499-0671
- ORCID 공개 API works 목록: https://pub.orcid.org/v3.0/0000-0001-9499-0671/works (2026-10-07 확인)
- 2026년 duration 논문: https://doi.org/10.1002/for.70209
- working papers: https://arxiv.org/abs/2609.06422, https://arxiv.org/abs/2607.25189, https://arxiv.org/abs/2607.20838
- ORCID의 논문 21건에 기존 홈페이지의 부동산 자동평가 논문 1건을 추가했습니다.
- 오래된 사이트와 제목/연도가 다른 경우 ORCID를 우선했습니다. 예: Price predictability는 ORCID에 2026년으로 기재되어 있으며 온라인 최초 공개는 2024년입니다.
- Risk-neutral option pricing의 ORCID 제목 오기는 arXiv의 동일 논문 정보를 바탕으로 model로 수정했습니다.
- 논문 제목은 sentence case로 통일하고 고유명사와 약어를 유지했습니다.
- arXiv 저자 페이지에서 대조한 학술지 논문 18편에 arXiv 링크를 병기했습니다.
- 사용자 요청에 따라 현재 연구 소개와 연구 관심 분야에서 machine learning을 제외했습니다. 과거 담당 과목과 출판 논문 제목은 유지합니다.
- Working papers는 3편입니다. Dropbox의 /Work/Github/ksublee-homepage에 최종본을 통합했습니다.
- 비공개 연구 원고, 학생 정보, 연구비/행정 내용은 포함하지 않았습니다.
