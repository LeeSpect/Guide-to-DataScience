우리가 원하는 HTML 요소의 CSS 선택자를 자동으로 가져올 수도 있습니다.

개발자 도구에서 특정 HTML 요소를 오른쪽 클릭하고 Copy 메뉴의 Copy Selector를 클릭하면, CSS 선택자가 클립보드에 복사됩니다.  
텍스트 에디터에 붙여넣기 해 보세요!

개발자 도구를 잘 활용하면 파싱이 좀 더 쉬워집니다.

이번에는 실제 웹사이트의 response를 받아서 파싱해 봅시다.

# HTML 코드 받아오기
웹사이트의 HTML 코드를 받아옵시다.
```
import requests

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

# 결과 출력
print(response.text)
```
```
출력 생략
```
# BeautifulSoup 타입으로 바꾸기
파싱을 위해서 HTML 코드를  BeautifulSoup 타입으로 바꿔야겠죠?
```
import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 결과 출력
print(soup)
```
```
출력 생략
```
# 태그 구조 파악하기
페이지 코드와 크롬 개발자 도구로 구조를 살펴봅시다.  
우리가 원하는 '인기 아티스트'라는 문자열은 h3 태그에 있네요.
```
<h3 class="popular__title">인기 아티스트</h3>
```
그리고 그 아래에 우리가 원하는 10명의 아티스트 이름이 있습니다.  
인기 아티스트를 모두 감싸는 태그는 'popular__order'라는 클래스를 가진 ```<ul>``` 태그입니다.
<img src="https://user-images.githubusercontent.com/64893709/95435762-f1668a80-098d-11eb-9675-f726fd986387.png" width="60%" height="50%"></img>   

그리고 그 안의 ```<li>``` 태그가 아티스트 이름을 담고 있네요.
<img src="https://user-images.githubusercontent.com/64893709/95435935-2d99eb00-098e-11eb-9b57-533d9bc00082.png" width="60%" height="50%"></img>   
이런 내용을 HTML 텍스트에서 찾아볼 수도 있겠죠? 편한 방식으로 하면 됩니다.  
우리가 원하는 정보는 이 부분에 있습니다.
```
<h3 class="popular__title">인기 아티스트</h3>
<ul class="popular__order">
<li class="list">
<span class="list__index blue">1</span> 아이유 (IU)
          </li>
<li class="list">
<span class="list__index blue">2</span> 방탄소년단
          </li>
<li class="list">
<span class="list__index blue">3</span> Red Velvet (레드벨벳)
          </li>
<li class="list">
<span class="list__index">4</span> IKON
          </li>
<li class="list">
<span class="list__index">5</span> 멜로망스
          </li>
<li class="list">
<span class="list__index">6</span> 다비치
          </li>
<li class="list">
<span class="list__index">7</span> 윤딴딴
          </li>
<li class="list">
<span class="list__index">8</span> 수지 (SUZY)
          </li>
<li class="list">
<span class="list__index">9</span> 김동률
          </li>
<li class="list">
<span class="list__index">10</span> 폴킴
          </li>
</ul>
```
처음에는 눈에 잘 들어오지 않더라도, HTML 코드의 구조를 파악하는 연습을 해야 합니다.  
시간을 갖고 천천히 구조를 살펴보세요.

공백과 엔터를 재배열 해보면, 사실 아래와 같은 구조입니다.
```
<h3 class="popular__title">인기 아티스트</h3>

<ul class="popular__order">
     <li class="list">
          <span class="list__index blue">1</span>
          아이유 (IU)
     </li>
     <li class="list">
          <span class="list__index blue">2</span>
          방탄소년단
     </li>
     <li class="list">
          <span class="list__index blue">3</span>
          Red Velvet (레드벨벳)
     </li>
     <li class="list">
          <span class="list__index">4</span>
          IKON
     </li>
     <li class="list">
          <span class="list__index">5</span>
          멜로망스
     </li>
     <li class="list">
          <span class="list__index">6</span>
          다비치
     </li>
     <li class="list">
          <span class="list__index">7</span>
          윤딴딴
     </li>
     <li class="list">
          <span class="list__index">8</span>
          수지 (SUZY)
     </li>
     <li class="list">
          <span class="list__index">9</span>
          김동률
     </li>
     <li class="list">
          <span class="list__index">10</span>
          폴킴
     </li>
</ul>
```
"popular__order"라는 클래스를 갖는 ```<ul>``` 태그가 있고, 그 아래에 10개의 ```<li>``` 태그가 있습니다.  
각 ```<li>``` 태그는 1개의 ```<span>``` 태그와 텍스트를 갖고 있습니다.  
```<span>``` 태그에는 순위가 들어 있네요.

# 태그 골라내기
이 HTML 태그에서 10명의 아티스트 이름을 선택하는 방법은 여러 가지가 있는데요.

'popular__order' 클래스를 가진 ```<ul>``` 태그에 중첩된 모든 ```<li>``` 태그를 선택해 봅시다.  
선택자를 .popular__order li라고 하면 되겠죠?
```
import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# "popular__order" 클래스를 가진 태그에 중첩된 모든 <li> 태그 선택
soup.select(".popular__order li")
```
```
[<li class="list">
 <span class="list__index blue">1</span> 아이유 (IU)
           </li>, <li class="list">
 <span class="list__index blue">2</span> 방탄소년단
           </li>, <li class="list">
 <span class="list__index blue">3</span> Red Velvet (레드벨벳)
           </li>, <li class="list">
 <span class="list__index">4</span> IKON
           </li>, <li class="list">
 <span class="list__index">5</span> 멜로망스
           </li>, <li class="list">
 <span class="list__index">6</span> 다비치
           </li>, <li class="list">
 <span class="list__index">7</span> 윤딴딴
           </li>, <li class="list">
 <span class="list__index">8</span> 수지 (SUZY)
           </li>, <li class="list">
 <span class="list__index">9</span> 김동률
           </li>, <li class="list">
 <span class="list__index">10</span> 폴킴
           </li>]
```
```<li>``` 태그 10개의 리스트가 출력되었습니다.

우리는 각 ```<li>``` 태그 안에 있는 텍스트만 꺼내오고 싶습니다. text 메소드를 활용합시다.

그리고 리스트의 각 요소에 모두 적용하기 위해, for 반복문을 사용합니다.
```
import requests
from bs4 import BeautifulSoup

# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/music/index")

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# "popular__order" 클래스를 가진 태그에 중첩된 모든 <li> 태그 선택
li_tags = soup.select(".popular__order li")

# 빈 리스트 생성
popular_artists = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    popular_artists.append(li.text)

# 결과 출력
print(popular_artists)
```
```
['\n1 아이유 (IU)\n          ', '\n2 방탄소년단\n          ', '\n3 Red Velvet (레드벨벳)\n          ', '\n4 IKON\n          ', '\n5 멜로망스\n          ', '\n6 다비치\n          ', '\n7 윤딴딴\n          ', '\n8 수지 (SUZY)\n          ', '\n9 김동률\n          ', '\n10 폴킴\n          ']
```
여기에 앞뒤 공백만 제거하면 우리가 원하는 데이터만 골라낼 수 있겠네요.
```
# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    popular_artists.append(li.text.strip())

# 결과 출력
print(popular_artists)
```
```
['1 아이유 (IU)', '2 방탄소년단', '3 Red Velvet (레드벨벳)', '4 IKON', '5 멜로망스', '6 다비치', '7 윤딴딴', '8 수지 (SUZY)', '9 김동률', '10 폴킴']
```
