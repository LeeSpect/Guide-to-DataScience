실제 웹사이트의 복잡한 HTML 코드를 파싱하려면, CSS 선택자에 대해 좀 더 자세히 이해해야 합니다.

앞서 네 가지의 CSS 선택자를 알아봤는데요.  
여러 CSS 선택자를 조합해서 사용할 수도 있습니다.

# OR 연산
쉼표 (,)는 OR 연산을 의미합니다.  
두 CSS 선택자 중 하나라도 해당되면 선택합니다.

아래와 같은 HTML 코드가 있다고 해 봅시다.
```
<p class="one">paragraph 1</p>
<p class="two">paragraph 2</p>
<p class="three">paragraph 3</p>
<p class="four">paragraph 4</p>
<p class="five">paragraph 5</p>
```
여기에서 class 이름이 "two"이거나, class 이름이 "four"인 태그를 선택하려면 .two, .four라고 쓰면 됩니다.
```
.two, .four {
  color: red;
}
```
이 CSS 코드는 class 이름이 "two"이거나 "four"인 태그의 색상을 빨간색으로 지정하라는 의미입니다.

실행 결과로 살펴봅시다.   
<img src="https://user-images.githubusercontent.com/64893709/95431692-8fefed00-0988-11eb-8414-85daa15de928.png" width="60%" height="50%"></img>   
# AND 연산
OR 연산이 있으니 AND 연산도 있겠죠?  
두 CSS 선택자를 붙여쓰면, 두 조건에 모두 해당되는 요소만 선택합니다.

HTML 코드를 봅시다.
```
<p class="favorite">paragraph 1</p>
<p class="favorite">paragraph 2</p>
<p class="favorite private">paragraph 3</p>
<p class="private">paragraph 4</p>
<p class="private">paragraph 5</p>
```
여기에서 "favorite" 클래스와 "private" 클래스를 모두 가진 태그를 선택하려면, .favorite.private라고 붙여서 작성하면 됩니다.
```
.favorite.private {
  color: red;
}
```
이 CSS 코드는 "favorite" 클래스와 "private" 클래스를 모두 가진 태그의 색상을 빨간색으로 지정하라는 의미입니다.

실행 결과를 살펴봅시다.   
<img src="https://user-images.githubusercontent.com/64893709/95432070-1f959b80-0989-11eb-8792-86d9951c936b.png" width="60%" height="50%"></img>   
# 중첩된 요소
HTML 태그 안에 또 다른 HTML 태그가 있을 수 있습니다. 이런 경우 태그가 중첩되어 있다고 부르는데요.

일반적인 웹 페이지의 HTML 태그는 많이 중첩되어 있기 때문에, 중첩에 대한 조건을 추가하는 경우가 많습니다.

HTML 코드를 봅시다.
```
<i>디저트</i>
<p>
  <i>다쿠아즈</i>
  <i>마카롱</i>
  <i>케이크</i>
</p>
```
```<i>``` 태그는 텍스트를 기울이는 이탤릭 효과를 의미합니다.

HTML 코드에 여러 개의 ```<i>``` 태그가 있네요.  
모든 ```<i>``` 태그가 아닌, ```<p>``` 태그 안에 중첩된 ```<i>```태그만 가져오고 싶습니다.  
다시 말해 "디저트"는 제외하고, "다쿠아즈", "마카롱", "케이크"만 가져오려는 거죠.

이런 경우, 띄어쓰기로 중첩을 표현할 수 있습니다.

CSS 선택자를 p i라고 작성하면, ```<p>```태그 안에 중첩된 ```<i>```태그를 의미합니다.
```
p i {
  color: red;
}
```
이 CSS 코드는 <p>태그 안에 있는 ```<i>```태그만 빨간색으로 지정하라는 의미입니다.

실행 결과를 살펴봅시다.   
<img src="https://user-images.githubusercontent.com/64893709/95432471-aba7c300-0989-11eb-81dd-cd4e6f44372e.png" width="60%" height="50%"></img>   
