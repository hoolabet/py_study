# pip install selenium beautifulsoup4 로 라이브러리 설치
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import re
# pip install konlpy==0.5.1
# pip install jpype1
# pip install Jpype1-py3
from konlpy.tag import Okt
from collections import Counter


# 크롤링할 사이트 주소를 정의합니다.
source_url = "https://namu.wiki/RecentChanges"

#options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 사이트의 html 구조에 기반하여 크롤링을 수행합니다.
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # for Windows
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # for Windows
driver.get(source_url)
driver.implicitly_wait(10)
table_rows = driver.find_elements(By.XPATH,'//*[@id="C6Rc9QlVe"]/div[2]/div/div/div/div/div/article/div[3]/div/div/div/div[1]/div/div/table/tbody/tr/td[1]/a[1]')
# table_rows = driver.find_elements(By.XPATH,'//*[@id="C6Rc9QlVe"]/div[2]/div/div/div/div/div/article/div[3]/div/div/div/div[1]/div/div/table/tbody/tr')
# print(table_rows)
page_urls = []

# #for i in range(0,len(table_rows)): # 시간이 너무 오래 걸림
# for i in range(0,5):    # 어차피 맨 밑에 상위 다섯번째까지만 출력하면 되니 5번만 반복.
#     first_td=table_rows[i].find_elements(By.TAG_NAME,"td")
#     td_url=first_td[0].find_elements(By.TAG_NAME,"a")
#     if len(td_url) >0 :
#         page_url=td_url[0].get_attribute("href")
#         #page_url=table_rows[0].get_attribute("href")   # a태그의 href 속성을 리스트로 추출하여, 크롤링 할 페이지 리스트를 생성합니다.
#         print(page_url)
#         if 'png' not in page_urls:
#             page_urls.append(page_url)

for i in range(0,5):    # 어차피 맨 밑에 상위 다섯번째까지만 출력하면 되니 5번만 반복.
    page_url=table_rows[i].get_attribute("href")
    if 'png' not in page_urls:
        page_urls.append(page_url)


columns = ['title','category','content_text']
df=pd.DataFrame(columns=columns)

for page_url in page_urls:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get(page_url)
    req=driver.page_source
    soup=BeautifulSoup(req,"html.parser")
    contents_table=soup.find(attrs={"class":"SVuqC-pU"})
    title=contents_table.find_all("h1")[0]

    if len(contents_table.find_all("ul"))>0:
        category=contents_table.find_all("ul")[0]
    else:
        category=None

    content_paragraphs=contents_table.find_all(name="div", attrs={"class":"UtCm7-qJ"})
    content_corpus_list=[]

    if title is not None:
        row_title=title.text.replace("\n"," ")
    else:
        row_title=""
    
    if content_paragraphs is not None:
        for paragraghs in content_paragraphs:
            if paragraghs is not None:
                content_corpus_list.append(paragraghs.text.replace("\n"," "))
            else:
                content_corpus_list.append("")
    else:
        content_corpus_list("")

    if category is not None:
        row_category=category.text.replace("\n"," ")
    else:
        row_category=""

    row=[row_title,row_category,"".join(content_corpus_list)]
    series=pd.Series(row, index=df.columns)
    df=df.append(series, ignore_index=True)




    driver.close()



def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글의 정규표현식을 나타냅니다.
    result = hangul.sub('', text)
    return result

#print(text_cleaning(df["content_text"][0]))
# df["title"]=df["title"].apply(lambda x:text_cleaning(x))
# df["category"]=df["category"].apply(lambda x:text_cleaning(x))
# df["content_text"]=df["content_text"].apply(lambda x:text_cleaning(x))
for column in columns:
    df[column] = df[column].apply(lambda x:text_cleaning(x))

#print(df.head(5))

title_corpus="".join(df["title"].tolist())
category_corpus="".join(df["category"].tolist())
content_corpus="".join(df["content_text"].tolist())

# print(title_corpus)
# print(category_corpus)
# print(content_corpus)


nouns_tagger = Okt()
nouns = nouns_tagger.nouns(content_corpus)
count = Counter(nouns)
# print(count)
remove_char_counter=Counter({x : count[x] for x in count if len(x)>1})
# print(remove_char_counter.most_common())
# remove_char_counter_list = [f"{k} : {v}" for (k,v) in remove_char_counter.items() if v > 100]
# for i in remove_char_counter_list:
#     print(i)

stopwords = []
korean_stopwords_path = "python-data-analysis-master/data/korean_stopwords.txt"
with open(korean_stopwords_path, encoding="utf-8") as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]
# print(stopwords[:10])

namu_wiki_stopwords = ["상위", "문서", "문단", "이전", "문제", "내용", "누설", "아래", "해당", "설명", "표기", "추가", "모든", "사용", "매우", "가장", "줄거리"
    , "요소", "상황", "편집", "틀", "경우", "때문", "모습", "정도", "이후", "사실", "생각", "인물", "이름", "년월"]

for stopword in namu_wiki_stopwords:
    stopwords.append(stopword)

remove_char_counter = Counter({x : remove_char_counter[x] for x in count if x not in stopwords})
print(remove_char_counter.most_common())

import random
import pytagcloud # pygame  => pygame-2.1.2-cp311-cp311-win_amd64.whl cmd install
import webbrowser
import datetime

now = datetime.datetime.now()
nowStr = now.strftime("%Y_%m_%d_%H_%M_%S")

ranked_tags = remove_char_counter.most_common(40)

taglist = pytagcloud.make_tags(ranked_tags, maxsize=80)

pytagcloud.create_tag_image(taglist, f"wordcloud_{nowStr}.jpg", size=(900, 600), fontname="NanumGothic", rectangular=False)
