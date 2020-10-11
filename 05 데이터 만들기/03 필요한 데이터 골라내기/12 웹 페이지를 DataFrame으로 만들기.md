데이터 가져오기의 마지막 단계에 도착했습니다.  
우리가 원하는 데이터를 DataFrame으로 만들면 앞서 배웠던 시각화나 분석 등 다양하게 활용할 수 있겠죠?

[SSG](http://www.ssg.com/)의 검색 결과를,

<img src="https://user-images.githubusercontent.com/64893709/95673888-77c9d900-0be7-11eb-9fc7-6b4227da135d.png" width="60%" height="50%"></img>

이런 DataFrame으로 만들어 봅시다.

<img src="https://user-images.githubusercontent.com/64893709/95673943-e27b1480-0be7-11eb-88dd-8294083b43e1.png" width="60%" height="50%"></img>

# DataFrame을 만드는 방법

어떻게 하면 DataFrame을 만들 수 있을까요?  
DataFrame을 만드는 방법에는 여러 가지가 있고, 그중 하나는 리스트를 담은 리스트였습니다.  
기억이 잘 안 나시는 분은 [이전 레슨](https://github.com/LeeSpect/Guide-to-DataScience/blob/master/01%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%82%AC%EC%9D%B4%EC%96%B8%EC%8A%A4%20%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0/Pandas/15%20create%20DataFrame.py)을 참고해 보세요.

우리는 웹 페이지에서 상품의 정보를 파싱한 뒤, 리스트를 담은 리스트 형태로 저장할 겁니다.

# DataFrame 설계하기

먼저 하나의 레코드(row)에 대한 설계를 합니다.  
column이 "이름", "가격", "이미지 주소" 총 세 개니까, 다음과 같은 형태로 만들면 되겠네요.
```
["이름 1", "가격 1", "이미지 주소 1"]
```
그리고 이 레코드가 여러 개 모이면, DataFrame을 만들 수 있겠죠?  
우리가 결국 원하는 형태는 이런 형태입니다.
```
[["이름 1", "가격 1", "이미지 주소 1"], 
["이름 2", "가격 2", "이미지 주소 2"], 
["이름 3", "가격 3", "이미지 주소 3"]]
```
# 파싱하기
이제 방법을 알았으니, 데이터를 파싱해서 DataFrame으로 만들어 봅시다.
```
import time
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.csrch_tip')) == 0:
        product_names = soup.select('.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko')
        product_prices = soup.select('.cunit_info > div.cunit_price.notranslate > div.opt_price > em')
        product_urls = soup.select('.cunit_prod > div.thmb > a > img')
        page_num += 1
        time.sleep(3)

        # 여기에 각 상품의 정보를 하나의 레코드로 저장하는 코드 추가

    else:
        break
```
페이지에 있는 모든 상품 이름은 product_names에, 상품 가격은 product_prices에, 이미지 링크는 product_urls에 저장했습니다.

이제 각 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가합니다.  
(이미지 주소는 "http://www.ssg.com" 이후부터 나오기 때문에, "http://www.ssg.com"를 붙여 줍니다.)
```
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.csrch_tip')) == 0:
        product_names = soup.select('.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko')
        product_prices = soup.select('.cunit_info > div.cunit_price.notranslate > div.opt_price > em')
        product_urls = soup.select('.cunit_prod > div.thmb > a > img')
        page_num += 1
        time.sleep(3)
        
        # 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가하기
        for i in range(len(product_names)):
            record = []
            record.append(product_names[i].text)
            record.append(product_prices[i].text.strip())
            record.append("https://www.ssg.com" + product_urls[i].get('src'))
            records.append(record)
    else:
        break

# 결과 출력
print(len(records))
print(records)
```
```
545
[['[다운로드 번호]★★★ 모여봐요 동물의 숲★★★', '64,800', 'https://www.ssg.com//item.ssgcdn.com/02/99/91/item/1000040919902_i1_232.jpg'], ['[닌텐도 스위치] 슈퍼마리오 파티', '55,080', 'https://www.ssg.com//item.ssgcdn.com/10/84/53/item/1000029538410_i1_232.jpg'], ['[다운로드 번호]★★★ 모여봐요 동물의 숲★★★', '63,504', 'https://www.ssg.com//item.ssgcdn.com/94/97/91/item/1000040919794_i1_232.jpg'], ... ]
```
데이터가 잘 저장되었습니다.
# DataFrame 만들기

이제 DataFrame 형태로 만들어주면 됩니다. pandas의 문법은 익숙하죠?
```
import pandas as pd

# DataFrame 만들기
df = pd.DataFrame(data = records, columns = ["이름", "가격", "이미지 주소"])

# DataFrame 출력
df.head()
```
완성된 전체 코드는 다음과 같습니다.
```
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

# 빈 리스트 생성
records = []

# 시작 페이지 지정
page_num = 1

while True:
    # HTML 코드 받아오기
    response = requests.get("http://www.ssg.com/search.ssg?target=all&query=nintendo&page=" + str(page_num))

    # BeautifulSoup 타입으로 변형하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # "prodName" 클래스가 있을 때만 상품 정보 가져오기
    if len(soup.select('.csrch_tip')) == 0:
        product_names = soup.select('.cunit_info > div.cunit_md.notranslate > div > a > em.tx_ko')
        product_prices = soup.select('.cunit_info > div.cunit_price.notranslate > div.opt_price > em')
        product_urls = soup.select('.cunit_prod > div.thmb > a > img')
        page_num += 1
        time.sleep(3)
        
        # 상품의 정보를 하나의 레코드로 만들고, 리스트에 순서대로 추가하기
        for i in range(len(product_names)):
            record = []
            record.append(product_names[i].text)
            record.append(product_prices[i].text.strip())
            record.append("https://www.ssg.com" + product_urls[i].get('src'))
            records.append(record)
    else:
        break

# DataFrame 만들기
df = pd.DataFrame(data = records, columns = ["이름", "가격", "이미지 주소"])

# DataFrame 출력
df.head()
```
