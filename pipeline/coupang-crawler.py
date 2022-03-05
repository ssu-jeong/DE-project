# from calendar import c
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib import parse
import re

#by-6mini
#검색목록 크롤링
def getPageString(url):
    data = requests.get(url, headers=headers)
    return data.content


def getProducts(string):

    bs = BeautifulSoup(string, "html.parser")
    base_url = 'https://www.coupang.com/'
    item_list = bs.select('ul#productList li')

    for item in item_list:
        #상품이름
        div_name = item.find("div", {"class":"name"})
        name = div_name.getText()

        #url
        url = item.select_one('a').get('href')
        url = parse.urljoin(base_url, url)

        #image
        dt_image = item.find("dt", {"class":"image"})
        image = dt_image.find("img").get('src')
        img_url = parse.urljoin(base_url, image)

        #price
        price = item.find("strong", {"class":"price-value"}).getText()
        price = int(re.sub(',', '', price))
        
        res.append([name, url, img_url, price])

def saveCsv(list):
    filename = '쿠팡조회결과re.csv'
    df = pd.DataFrame(list, columns = ['name', 'url', 'img_url', 'price'])
    df.to_csv(filename, index=False, encoding='UTF-8')
    

        
if __name__ == '__main__':

    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}

    res = [] # 최종
    count = 1
    while count < 28: # 페이지 설정 27 
        url = 'https://www.coupang.com/np/search?q=%EB%B9%84%EA%B1%B4&page={}'.format(count)
        pageString = getPageString(url)

        # list append
        getProducts(pageString)

        count += 1

    # csv 저장
    saveCsv(res)
