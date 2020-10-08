BeautifulSoup 태그에 .text를 붙여서, 텍스트를 추출할 수 있었습니다.  
이번에는 태그의 속성 값을 추출해 봅시다.

```<img>``` 태그의 src 속성에는 일반적으로 이미지 주소가 저장되어 있습니다.  
이미지 주소를 받아와 볼건데요.  
```<img>``` 태그를 먼저 가져와야겠죠?
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

# 모든 <img> 태그 선택하기
img_tags = soup.select('img')

# 결과 출력
print(img_tags)
```
```
[<img alt="coffee" src="https://i.imgur.com/bY0l0PC.jpg"/>, <img alt="green-tea" src="https://i.imgur.com/fvJLWdV.jpg"/>, <img alt="milk" src="https://i.imgur.com/rNOIbNt.jpg"/>]
```
모든 <img> 태그를 리스트로 가져왔네요.  
첫 번째 <img> 태그만 꺼내 봅시다.
```
# 모든 <img> 태그 선택하기
img_tags = soup.select('img')

# 첫 번째 요소 출력하기
print(img_tags[0])
```
```
<img alt="coffee" src="https://i.imgur.com/bY0l0PC.jpg"/>
```
태그에 .text를 붙이면 텍스트가 추출된 것처럼, 태그에 ["속성 이름"]을 붙여주면 해당 속성의 값을 가져올 수 있습니다.  
이미지 주소는 src라는 속성에 저장되어 있으니, ["src"]라고 붙이면 되겠네요.
```
# 모든 <img> 태그 선택하기
img_tags = soup.select('img')

# 첫 번째 요소의 "src" 속성 값 가져오기
print(img_tags[0]["src"])
```
```
https://i.imgur.com/bY0l0PC.jpg
```
이미지 주소만 추출되었습니다.

for 반복문을 활용하면, 모든 이미지 주소를 한번에 가져올 수 있겠죠?
```
# 모든 <img> 태그 선택하기
img_tags = soup.select('img')

# 빈 리스트 만들기
img_srcs = []

# 이미지 주소 추출해서 리스트에 담기
for img in img_tags:
    img_srcs.append(img["src"])

# 결과 출력
print(img_srcs)
```
['https://i.imgur.com/bY0l0PC.jpg', 'https://i.imgur.com/fvJLWdV.jpg', 'https://i.imgur.com/rNOIbNt.jpg']
```
전체 코드는 다음과 같습니다. 직접 코드를 작성하고 실행해 보세요!
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

# 모든 <img> 태그 선택하기
img_tags = soup.select('img')

# 빈 리스트 만들기
img_srcs = []

# 이미지 주소 추출해서 리스트에 담기
for img in img_tags:
    img_srcs.append(img["src"])

# 결과 출력
print(img_srcs)
```
```
['https://i.imgur.com/bY0l0PC.jpg', 'https://i.imgur.com/fvJLWdV.jpg', 'https://i.imgur.com/rNOIbNt.jpg']
```
