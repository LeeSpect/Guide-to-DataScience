# 파싱(Parsing)이란?
'파싱'이란 문자의 구조를 분석해서 원하는 정보를 얻어내는 걸 말합니다.  
복잡한 HTML 코드에서 정보를 뽑아내는 것도 파싱의 일종이죠.

아래의 HTML 코드에서 '커피', '녹차', '우유'라는 텍스트 데이터를 추출한다고 해 봅시다.
```
<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습!</h2>

<p>이것은 첫 번째 문단입니다.</p>
<p>이것은 두 번째 문단입니다!</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>
```
물론 짧은 HTML 코드에서는 눈으로 확인하고 옮겨적을 수 있겠지만, 우리가 원하는 데이터는 훨씬 클테니 수작업을 할 수 없겠죠.

이럴 때 파싱이 필요합니다.

# Beautiful Soup
파이썬에서는 Beautiful Soup이라는 툴로 HTML을 파싱합니다.

파싱할 HTML 코드를 변수 html_code에 넣어줍시다. (파이썬에서 여러 줄의 텍스트를 """와 """사이에 두면, 하나의 문자열로 인식합니다.)
```
html_code = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습!</h2>

<p>이것은 첫 번째 문단입니다.</p>
<p>이것은 두 번째 문단입니다!</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>"""
```

## 1. BeautifulSoup 타입 만들기
HTML 코드를 파싱하려면, 먼저 HTML 코드를 'BeautifulSoup 타입'으로 바꿔줘야 합니다.  
bs4 라이브러리의 BeautifulSoup을 불러옵니다.
```
from bs4 import BeautifulSoup
```
불러온 BeautifulSoup에 HTML 코드를 넘겨주면, HTML 코드가 'BeautifulSoup 타입'으로 바뀝니다.  
HTML을 파싱한다는 의미로 'html.parser'을 함께 넘겨주세요.
```
# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(html_code, 'html.parser')

# type 출력
print(type(soup))
```
```
<class 'bs4.BeautifulSoup'>
```
type이 bs4.BeautifulSoup이라고 나오죠? 'BeautifulSoup 타입'으로 잘 바뀌었습니다.

## 2. 특정 태그 선택하기
BeautifulSoup 타입에는 .select() 메소드를 쓸 수 있습니다.  
'선택한다'는 의미인데, 괄호 안에 CSS 선택자를 넣으면 특정 HTML 태그만 선택할 수 있습니다.

예를 들어, 모든 ```<li>``` 태그를 가져오고 싶으면 CSS 선택자 'li'를 넘겨주면 됩니다.
```
# 모든 <li> 태그 선택하기
li_tags = soup.select('li')

# 결과 출력
print(li_tags)
```
```
[<li>커피</li>, <li>녹차</li>, <li>우유</li>]
```
그러면 전체 HTML 코드 중에 ```<li>``` 태그만 모아서 리스트로 출력됩니다.

리스트니까 하나씩 꺼낼 수 있겠죠?  
첫 번째 ```<li>``` 태그만 꺼내봅시다.
```
# 모든 <li> 태그 선택하기
li_tags = soup.select('li')

# 첫 번째 요소 출력하기
print(li_tags[0])
```
```
<li>커피</li>
```
첫 번째 ```<li>``` 태그만 잘 출력됩니다.

이렇게 Beautiful Soup을 사용하면 복잡한 HTML 코드에서 우리가 원하는 태그만 골라낼 수 있습니다.

## 3. 태그에서 문자열 추출하기
.select()로 가져온 태그는, 사실 그냥 텍스트가 아닙니다.  
타입을 확인해 봅시다.
```
# 모든 <li> 태그 선택하기
li_tags = soup.select('li')

# 첫 번째 요소 type 출력하기
print(type(li_tags[0]))
```
```
<class 'bs4.element.Tag'>
```
type이 bs4.element.Tag라고 나오죠? 그냥 ```"<li>커피</li>"```라는 텍스트와는 전혀 다른 결과물입니다. 이걸 BeautifulSoup 태그라고 부릅시다.

이렇게 만들어진  BeautifulSoup 태그에는 여러 기능이 있는데, 그 중 하나가 텍스트 추출입니다. (다른 기능은 조만간 배워봅시다.)  
BeautifulSoup 태그 뒤에 .text라고 붙이면, 텍스트만 꺼낼 수 있습니다.
```
# 모든 <li> 태그 선택하기
li_tags = soup.select('li')

# 첫 번째 <li> 태그 출력하기
print(li_tags[0])

# 첫 번째 <li> 태그의 텍스트 출력하기
print(li_tags[0].text)
```
```
<li>커피</li>
커피
```
드디어 우리가 원하는 '순수한 문자열'을 추출하는데 성공했습니다!

반복문을 사용하면, 모든 문자열을 추출해서 리스트에 담을 수 있겠죠?
```
# 모든 <li> 태그 선택하기
li_tags = soup.select('li')

# 빈 리스트 만들기
beverage_names = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    beverage_names.append(li.text)

# 결과 출력
print(beverage_names)
```
```
['커피', '녹차', '우유']
```
이 과정의 전체 코드는 다음과 같습니다.
```
from bs4 import BeautifulSoup

html_code = """<!DOCTYPE html>
<html>
<head>
    <title>Sample Website</title>
</head>
<body>
<h2>HTML 연습!</h2>

<p>이것은 첫 번째 문단입니다.</p>
<p>이것은 두 번째 문단입니다!</p>

<ul>
    <li>커피</li>
    <li>녹차</li>
    <li>우유</li>
</ul>

<img src='https://i.imgur.com/bY0l0PC.jpg' alt="coffee"/>
<img src='https://i.imgur.com/fvJLWdV.jpg' alt="green-tea"/>
<img src='https://i.imgur.com/rNOIbNt.jpg' alt="milk"/>

</body>
</html>"""

# BeautifulSoup 타입으로 변환
soup = BeautifulSoup(html_code, 'html.parser')

# 모든 <li> 태그 선택하기
li_tags = soup.select('li')

# 빈 리스트 만들기
beverage_names = []

# 텍스트 추출해서 리스트에 담기
for li in li_tags:
    beverage_names.append(li.text)

# 결과 출력
print(beverage_names)
```
```
['커피', '녹차', '우유']
```








