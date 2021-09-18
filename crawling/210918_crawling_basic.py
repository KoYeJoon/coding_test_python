# pip install webdriver-manager
# pip3 install selenium
# pip3 install beautifulsoap4
# pip3 install pandas

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup as bs
def crawl_page(URL, file_name):
    # driver를 chrome으로 설정
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # browser에서 특정 URL에 접근 / 페이지가 로드될 때까지 암시적 대기
    driver.get(URL)
    driver.implicitly_wait(2)

    # 페이지의 소스를 html이라는 변수가 가리키게 함
    html = driver.page_source
    with open(file_name, 'w') as f:
        f.write(html)

    # 작업이 끝나면 browser 종료
    driver.close()

    return html

html = crawl_page('https://search.shopping.naver.com/best100v2/detail.nhn?catId=50000000', 'naver_shopping.txt')
soup = bs(html, 'html.parser')

div_target = soup.find_all('div', {'id' : 'productListArea'})
li_target = soup.find_all('li',{'class':'_itemSection'})
item_list = []


for target in li_target:
    name = target.find('img')['alt']
    price = target.find('span', {'class', 'num'}).text
    item = {}
    item['name'] = name
    item['low_price'] = price
    item_list.append(item)

    print(f"name: {name}, low price: {price}")


import pandas as pd
df = pd.DataFrame(item_list)
print(df)