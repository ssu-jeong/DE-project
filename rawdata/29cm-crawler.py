from selenium import webdriver
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException

# chromer options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


# Variables
category_list = {
                    "266100100" : "뷰티",
                    "268100100" : "여성의류",
                    "272100100" : "남성의류", 
                    "269100100" : "여성가방", 
                    "256100100" : "홈", 
                    "273100100" : "남성가방", 
                    "270100100" : "여성신발", 
                    "74100100"  : "남성신발",
                    "271100100" : "여성액세서리", 
                    "275100100" : "남성액세서리", 
                    "265100100" : "컬처", 
                    "258100100" : "테크"
                }

button = "#wrap > section > ui-search > div > div > ui-search-product > div > div >\
            div.category_lst > div.product_content > ruler-basic-pagination > div >\
            span.pagination-next > a > ruler-svg-icon-next"

path = '/Users/chromedriver'            # chromedriver의 절대경로
driver = webdriver.Chrome(path)
driver.implicitly_wait(3)               # 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.


# 카테고리별 페이지 접근 함수 -> url리스트 뽑기.
def launcher(categories):
    urlList = []
    for code in categories:
        url = "https://search.29cm.co.kr/?keyword=%EB%B9%84%EA%B1%B4&page=1&\
                brandPage=1&type=product&category_large_code={}".format(code)
        urlList.append(url)
    return urlList


# 아이템리스트 추출 함수
def getItemList():
    #아이템 리스트 가져오기
    item_list = driver.find_elements_by_class_name('item_info')
    # print('상품개수: {}'.format(len(item_list)))

    for item in item_list:

        brandName = item.find_element_by_class_name("info_brand").text
        # print(brandName)
        name = item.find_element_by_class_name('info_name').text
        # print(name)
        price = item.find_element_by_class_name('num').text
        # print(price)
        item_url = item.find_element_by_class_name('info_desc').get_attribute('href')
        # print(item_url)
        # img_url = item.find_element_by_tag_name('img').get_attribute('src')

        res.append([brandName,name,price,item_url,category_num])

# to CSV
def saveCsv(list):
    filename = '29cm상품데이터.csv'
    df = pd.DataFrame(list, columns = ['brandName', 'name','price','item_url','category'])
    df.to_csv(filename, index=False, encoding= 'UTF-8')


#===================================== Main Method =====================================#
res = []
for i in launcher(category_list.keys()):

    category_num = category_list[i.split("=")[-1]] 
    driver.get(i)
    # print("============" + i + "================")

    while True:
        try:
            # 다음 페이지 버튼
            nextBtn = driver.find_element_by_css_selector(button)

            # 다음 페이지 버튼 활성화 여부
            isExistNextPage = nextBtn.is_enabled()
            
            if isExistNextPage == True:
                getItemList()       # 현 페이지 크롤링
                nextBtn.click()     # 다음 페이지로 이동
                time.sleep(3)       # 페이지 이동 후 3초 버퍼링
                continue

        except NoSuchElementException as e:
            getItemList()
            break

saveCsv(res)
#======================================================================================#


# category_list = [
#                     '266100100', '268100100', '272100100', '269100100', 
#                     '256100100', '273100100', '270100100', '74100100', 
#                     '271100100', '275100100', '265100100', '258100100'
#                 ]