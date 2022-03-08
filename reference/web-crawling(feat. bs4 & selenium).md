## 웹 크롤링 (feat. bs4 & selenium)

---

### beautifulsoup

---

#### 1.setup

```py
from bs4 import BeautifulSoup
from urllib.request import urlopen

import csv 
import requests
import re 

# 내가 데이터를 가져오고자 하는 url
crawling_url = "https://www.billboard.com/charts/hot-100"

# http get request를 통해 url 내에 있는 데이터를 가져온다.
req = requests.get(crawling_url) 

# html 소스 가져오기(request를 통해 가져온 데이터를 문자열 객체str로 반환) 
# HTTP요청 결과로 받아온 HTML, 크롬 개발자 도구의 페이지 소스 내용과 동일
html = req.text

#bs4로 데이터를 python이 이해할 수 있는 구조로 parsing한다.
bs = BeautifulSoup(html, 'html.parser') 
```

    * content 속성
    가끔 beautifulsoup 객체를 만들 때 아래와 같이 첫 번째 인자에 content를 붙여주는 경우가 있다. content 속성에는 텍스트 형태의 HTML이 들어있게 된다. 그러니까 위에서 html소스 가져온 부분(.text 붙인)을 요 단계로 추릴 수도 있는 것이다.

    response = requests.get("https://www.billboard.com/charts/hot->100")
    soup = BeautifulSoup(response.content, 'html.parser')   

#### 2. element 접근

##### - object.select()

object라고 쓴 이유는 내가 만든 beautifulsoup 객체 이름에 따라서 해당 부분의 이름이 바뀔 수 있기 때문이다.

##### - select의 return

객체의 select 메소드를 통해 나온 결과는 리스트이다. 따라서

- 인덱스를 지정하여 text로 변환
- for loop를 돌려서 요소를 하나씩 꺼내기

위 두 가지 방법을 통해야만 사람이 볼 수 있는 형태로 확인이 가능하다.

##### - python shell 활용하기

크롤링할 때 python shell로 돌려보면 각 코드를 확인하기 편리하다. 

shell에서 모듈을 import하고 url get 등 조건을 만들고 시작하면, 결국 interactive 환경에서 내가 쓰는 메소드가 결과값을 return하는지 잘 확인할 수 있다. 
어느 줄의 결과가 어떤지 즉각적으로 확인할 수 있다.

### selenium

---

동적인 환경에서 크롤링을 해야 한다면 써야 하는 프레임워크. 코드를 통해 자동으로 컴퓨터가 클릭하게 만들거나, 텍스트 입력 엔터 등 브라우저를 제어할 수 있도록 한다. 

#### 1.setup

```py
import time
from selenium import webdriver
import requests
```

webdriver api를 통해 브라우저를 제어할 수 있다. 내 크롬 버전을 확인한 뒤에 크롬 드라이버 버전을 맞추어 다운받고, sciprt에 다운받은 경로를 지정해준다.

#### 2.element 접근

개발자 도구에서 원하는 코드 우클릭하면 내가 긁어오고 싶은 부분의 코드가 있고, 코드에서 우클릭했을 때 copy에서 element, selector, xpath 중 무엇을 가져올 것인지 선택할 수 있다.

##### - driver.page_source

브라우저에 보이는 그대로의 HTML, 크롬 개발자 도구의 Element 탭 내용과 동일하다. 페이지의 모든 elements 가져오기 기능으로 보면 될듯! 나는 잘 사용하지 않았지만 알아두면 좋을 것 같아서 우선 정리해놓았다.

```py
html = driver.page_source 
```

#### Reference

---
- [웹 크롤링(feat. bs4 & selenium)](https://velog.io/@matisse/%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81)