# 첫 번째 CSS 선택자: 태그 이름
하나의 CSS 코드를 살펴봤습니다.
```
li {
  color: blue;
  font-size: 20px;
}
```
이 코드의 의미는 "모든 <li> 태그의 색깔은 파란색으로, 크기는 20px로 하라"는 내용이었죠.

여기서 하나의 원리를 알 수 있습니다.  
CSS 선택자로 '태그의 이름'을 쓰면, 그 태그 모두에 스타일이 입혀집니다.

예를 들어 CSS 선택자에 해당하는 li를 p로 바꾸면,
```
p {
  color: blue;
  font-size: 20px;
}
```
모든 <p> 태그에 스타일이 적용됩니다.  
"모든 <p> 태그의 색깔은 파란색으로, 크기는 20px로 하라"는 내용이 되는 거죠.

실행 예시를 봅시다.   
<img src="https://user-images.githubusercontent.com/64893709/95423789-a42ded00-097c-11eb-8fe8-3c7db1b27600.png" width="60%" height="50%"></img>   
CSS 선택자로 태그의 이름을 쓰면, 그 태그 모두에 스타일이 입혀진다는 걸 확인했습니다.

# 두 번째 CSS 선택자: 아이디 (id)
모든 태그가 아닌, 단 하나의 태그에만 스타일을 입히고 싶으면 어떻게 할까요?  
'아이디(id)'라는 속성을 사용하면 됩니다. HTML 태그의 속성은 이전 챕터에서 살펴봤죠?

아래와 같은 식으로, HTML 태그에 아이디(id)를 지정할 수 있습니다.
```
<li id="coffee">커피</li>
<li id="green-tea">녹차</li>
<li id="milk">우유</li>
```
아이디를 지정한다고 해서, ```<li>``` 태그의 모습이 갑자기 바뀌거나 하진 않습니다.  
CSS 코드를 적용하기 전까지는 말이죠.

아이디를 CSS 선택자로 활용하면, 그 아이디를 가진 태그에만 스타일이 입혀집니다.  
아이디를 상징하는 기호는 #인데, #coffee라고 하면 아이디가 coffee인 태그만 선택합니다.
```
#green-tea {
  color: blue;
  font-size: 20px;
}
```
위의 코드는 "아이디가 green-tea인 태그의 색깔을 파란색으로, 크기를 20px로 하라"는 의미입니다.

실행 결과를 봅시다.   
<img src="https://user-images.githubusercontent.com/64893709/95424539-be1bff80-097d-11eb-8673-8308eb618464.png" width="60%" height="50%"></img>   
단, 동일한 아이디를 여러 태그가 가질 수 없다는 점 참고하세요!  
하나의 아이디는 HTML 코드 전체에 단 한 번만 나와야 합니다.

# 세 번째 CSS 선택자: 클래스(class)
아이디는 딱 하나의 HTML 태그만 선택할 수 있습니다.  
그럼 여러 태그에 동시에 스타일을 입히려면 어떻게 하면 될까요?

만약 아래 코드와 같이, 동일한 아이디가 여러 번 사용된다면 잘못된 코드입니다.
```
<li id="favorite">커피</li>
<li>녹차</li>
<li id="favorite">우유</li>
```
이런 상황에서 쓸 수 있는 '클래스(class)'라는 속성이 있습니다.  
클래스는 여러 HTML 태그에 공통으로 적용할 수 있습니다.
```
<li class="favorite">커피</li>
<li>녹차</li>
<li class="favorite">우유</li>
```
지금은 아이디보다 클래스가 더 적합하죠.  
클래스를 활용해서 스타일링하면, 여러 태그 동시에 스타일을 입힐 수 있습니다.

클래스를 상징하는 기호는 .인데, .favorite라고 하면 클래스가 favorite인 모든 태그를 선택할 수 있습니다.
```
.favorite {
  color: blue;
  font-size: 20px;
}
```
위의 코드는 "클래스가 favorite인 태그의 색깔을 파란색으로, 크기를 20px로 하라"는 의미입니다.

코드 실행 결과를 봅시다.
<img src="https://user-images.githubusercontent.com/64893709/95425356-1d2e4400-097f-11eb-94bc-0118c022d2d2.png" width="60%" height="50%"></img>   
하나의 태그는 아이디를 한 개만 가질 수 있습니다. 하지만 클래스는 여러 개를 가질 수 있습니다.  
클래스 이름 사이에 공백을 추가하면 됩니다.

예를 들어, <p> 태그에 "favorite", "preview" 두 개의 클래스를 모두 주고 싶다면 아래와 같이 작성하면 됩니다.
```
<p class="favorite preview">이것은 첫 번째 문단입니다.</p>
```
# 네 번째 CSS 선택자: 속성(attribute)
사실 아이디와 클래스도 속성 중 하나입니다.  
하지만 CSS 선택자로 워낙 많이 사용하기 때문에, #이나 . 처럼 쉽게 사용할 수 있는 문법이 있죠.

아이디와 클래스 외의 속성도 CSS 선택자로 사용할 수 있습니다.

예를 들어, ```<img>``` 태그에서 흔히 쓰는 alt 속성을 봅시다.  
alt 속성은 이미지가 로딩되지 않을 경우를 대비해서, 이 이미지가 어떤 이미지인지 텍스트로 알려주는 역할을 합니다.  
아래와 같이 사용할 수 있죠.
```
<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>
```
속성 이름과 속성 값을 CSS 선택자로 활용할 수 있습니다.  
[name="value"]의 형태로 적으면 됩니다.
```
[alt="green-tea"] {
  width: 300px;
}
```
위의 코드는 "alt 속성의 값이 "green-tea"인 태그의 가로 길이를 300px로 하라"는 의미입니다.

실행 결과를 살펴봅시다.
<img src="https://user-images.githubusercontent.com/64893709/95426722-536cc300-0981-11eb-8ad5-c4b5a664266e.png" width="60%" height="50%"></img>   
녹차에 대한 이미지만 가로 길이가 줄어든 것을 볼 수 있네요.

# CSS 선택자의 의미
기본적으로 CSS 선택자는 HTML 태그의 스타일을 지정하기 위해 사용합니다.  
하지만 추출할 데이터의 위치를 지정할 때도 활용할 수 있습니다. 웹 페이지의 원리를 역이용 하는거죠.
