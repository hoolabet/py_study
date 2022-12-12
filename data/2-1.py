# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import re

# excutable_path = "chromedriver.exe"

# source_url = "https://namu.wiki/RecentChanges"

# driver = webdriver.Chrome(executable_path=excutable_path)
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get(source_url)
# req = driver.page_source

# soup = BeautifulSoup(req, "html.parser")
# contents_table = soup.find(name="table")
# table_body = contents_table.find(name="tbody")
# table_rows = table_body.find_all(name="tr")

# page_url_base = "https://namu.wiki"
# page_urls = []

# for index in range(0, len(table_rows)):
#     first_td = table_rows[index].find_all("td")[0]
#     td_url = first_td.find_all("a")
#     if len(td_url) > 0:
#         page_url = page_url_base + td_url[0].get("href")
#         if "png" not in page_url:
#             page_urls.append(page_url)

# page_urls = list(set(page_urls))
# for page in page_urls[:3]:
#     print(page)

# excutable_path = "chromedriver.exe"

# source_url = "https://namu.wiki/RecentChanges"

# driver = webdriver.Chrome(executable_path=excutable_path)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get(source_url)
# req = driver.page_source

# soup = BeautifulSoup(req, "html.parser")
# contents_table = driver.find_elements(By.TAG_NAME, "table")
# print(contents_table)
# table_body = contents_table.find_elements(By.TAG_NAME, "tbody")
# table_rows = table_body.find_elements(By.TAG_NAME, "tr")
    
# page_url_base = "https://namu.wiki"
# page_urls = []

# for index in range(0, len(table_rows)):
#     first_td = table_rows[index].find_elements(By.TAG_NAME, "td")[0]
#     td_url = first_td.find_elements(By.TAG_NAME, "a")
#     if len(td_url) > 0:
#         page_url = page_url_base + td_url[0].get("href")
#         if "png" not in page_url:
#             page_urls.append(page_url)

# page_urls = list(set(page_urls))
# for page in page_urls[:3]:
#     print(page)

#------------------------------------------------------------------------------

# pip install selenium beautifulsoup4 로 라이브러리 설치
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# # 크롤링할 사이트 주소를 정의합니다.
# source_url = "https://namu.wiki/RecentChanges"

# # 사이트의 html 구조에 기반하여 크롤링을 수행합니다.
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # for Windows
# driver.get(source_url)
# driver.implicitly_wait(10)
# table_rows = driver.find_elements(By.XPATH,'//*[@id="C6Rc9QlVe"]/div[2]/div/div/div/div/div/article/div[3]/div/div/div/div[1]/div/div/table/tbody/tr/td/a')
# print(table_rows)

# page_urls = []
# for i in range(0,len(table_rows)):
#     page_urls.append(table_rows[i].get_attribute("href"))   # a태그의 href 속성을 리스트로 추출하여, 크롤링 할 페이지 리스트를 생성합니다.

# # 중복 url을 제거합니다.
# page_urls = list(set(page_urls))
# for page in page_urls[:3]:
#     print(page)

# # 크롤링에 사용한 브라우저를 종료합니다.
# driver.close()

# # 크롤링할 사이트 주소를 정의합니다.
# source_url = "https://www.naver.com"

# # 사이트의 html 구조에 기반하여 크롤링을 수행합니다.
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # for Windows
# driver.get(source_url)
# driver.implicitly_wait(10)
# table_rows = driver.find_elements(By.XPATH,'//*[@class="logo_special"]/a')
# print(table_rows)

# page_urls = []
# for i in range(0,len(table_rows)):
#     page_urls.append(table_rows[i].get_attribute("href"))   # a태그의 href 속성을 리스트로 추출하여, 크롤링 할 페이지 리스트를 생성합니다.

# # 중복 url을 제거합니다.
# page_urls = list(set(page_urls))
# for page in page_urls[:3]:
#     print(page)

# # 크롤링에 사용한 브라우저를 종료합니다.
# driver.close()

# 크롤링할 사이트 주소를 정의합니다.
source_url = "https://namu.wiki/RecentChanges"

# 사이트의 html 구조에 기반하여 크롤링을 수행합니다.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # for Windows
driver.get(source_url)
driver.implicitly_wait(10)
table_rows = driver.find_elements(By.XPATH,'//*[@id="C6Rc9QlVe"]/div[2]/div/div/div/div/div/article/div[3]/div/div/div/div[1]/div/div/table/tbody/tr/td/a[1]')
tr_rows = driver.find_elements(By.XPATH,'//*[@id="C6Rc9QlVe"]/div[2]/div/div/div/div/div/article/div[3]/div/div/div/div[1]/div/div/table/tbody/tr/td[1]/a[1]')

page_urls = []

for i in range(0,len(table_rows)):
    page_urls.append(table_rows[i].get_attribute("href"))   # a태그의 href 속성을 리스트로 추출하여, 크롤링 할 페이지 리스트를 생성합니다.

titles = []

for i in range(0, len(tr_rows)):
    titles.append(tr_rows[i].text)
title = titles[0]
print(titles)

# 중복 url을 제거합니다.
# page_urls = list(set(page_urls))
print("page_ urls : "+page_urls[0])
driver.close()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # for Windows
driver.get(page_urls[0])
driver.implicitly_wait(10)

li_table = driver.find_elements(By.XPATH, '//*[@id="C6Rc9QlVe"]/div[2]/div/div/div/div/div/div[1]/div[5]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/ul/li')
li2_table = driver.find_elements(By.XPATH, '//*[@class="k+DkxGOY"]')
content_table = driver.find_elements(By.XPATH, '//*[@class="i29dyTqj"]')

print(title)
li_list = []
for i in range(0,len(li_table)):
    li_list.append(li_table[i].text)
print(li_list)

li2_list = []
for i in range(0,len(li2_table)):
    li2_list.append(li2_table[i].text)
print(li2_list)

content_list = []
for i in range(0,len(content_table)):
    content_list.append(content_table[i].text)
print(content_list)

# 크롤링에 사용한 브라우저를 종료합니다.
driver.close()

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# for i in range(0,len(page_urls)):
#     driver.get(page_urls[i])
#     driver.implicitly_wait(5)
#     first_content = driver.find_elements(By.XPATH, '//*[@id="C6Rc9QlVe"]/div[2]/div/div/div/div/div/article/div[5]/div/div/div/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div/div/ul/li[1]/a[1]')
#     print(len(first_content))
# driver.close()



