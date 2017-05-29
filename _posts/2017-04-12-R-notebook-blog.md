---
layout: post
title: R noteboook을 이용한 블로그 
categories : Data Science
tags: [R]
---


<p>Notebook 형식의 장점은 작성한 notebook을 웹페이지 등에 쉽게 연동하여 띄울 수 있다는 점입니다.</p>
<p>지금의 페이지는 Rstudio에서 R notebook 파일로 작성된 후 html 파일로 변경하여 블로그에 올리는 과정을 통해 작성 되었습니다.</p>
<p>예제 코드 :</p>
<pre class="r"><code>coin_list = c(500, 100, 50, 10)

num_cases &lt;- function(money, coin){
  if (money == coin){
    return(1)
  } else if (money &lt; coin){
    return(0)
  } else {
    return(sum(sapply(coin_list[coin_list &lt;= coin], 
                      FUN = num_cases, 
                      money = money - coin)))
  }
}</code></pre>
<p>함수 실행 결과 확인하기</p>
<pre class="r"><code>num_cases(money = 120, coin = 100)</code></pre>
<pre><code>## [1] 1</code></pre>
<p>참고로 함수 내의 <code>sapply</code>는 다음의 원리를 통해 작동하게 됩니다.</p>
<ul>
<li><p>먼저 <code>sapply</code>에 적용되는 함수는 <code>FUN = num_cases</code>이므로 <code>num_cases</code>는 일종의 recursive 함수라는 것을 알 수 있습니다.</p></li>
<li><p>한편 <code>sapply</code>가 적용되는 벡터는 <code>sapply</code>의 첫번째 인자인 <code>coin_list[coin_list &lt;= coin]</code>입니다.</p></li>
<li><p><code>coin_list</code>는 함수 내에는 정의되지 않고, 전역 변수로서 존재합니다.</p></li>
<li><p>마지막으로 <code>money = money - coin</code>는 <code>num_cases</code> 함수의 첫번째 인자인 <code>money</code>가 되겠습니다.</p></li>
<li><p>정리하자면 함수 내의 <code>sapply</code>는 <code>num_cases</code>함수를 <code>coin_list[coin_list &lt;= coin]</code>의 각각의 원소에 적용하는데, 이 때<code>coin_list[coin_list &lt;= coin]</code>는 <code>num_cases</code> 함수의 두번째 인자입니다.</p></li>
<li><p>따라서 <code>num_cases</code> 함수의 첫번째 인자도 추가적으로 명시해야 하는데, 그것이 <code>sapply</code>의 마지막 인자인 <code>money = money - coin</code>가 됩니다.</p></li>
</ul>



