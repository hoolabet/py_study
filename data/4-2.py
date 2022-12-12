import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

source_url = "https://map.kakao.com"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(source_url)
# driver.implicitly_wait(10)
searchbox = driver.find_element(By.XPATH,'//*[@id="search.keyword.query"]')
searchbox.send_keys("강남역 고기집")

searchbutton = driver.find_element(By.XPATH,'//*[@id="search.keyword.submit"]')
driver.execute_script("arguments[0].click();", searchbutton)

time.sleep(2)

html = driver.page_source
soup=BeautifulSoup(html,"html.parser")
moreviews=soup.find_all(name="a", attrs={"class":"moreview"})

page_urls = []
for mv in moreviews:
    page_url = mv.get("href")
    print(page_url)
    page_urls.append(page_url)

driver.close()

columns = ['score', 'review']
df = pd.DataFrame(columns=columns)

options = webdriver.ChromeOptions() 
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for pu in page_urls:
    driver.get(pu)
    time.sleep(2)
    for i in range(0,5):
        try:
            another_reviews = driver.find_element(By.XPATH,f'//*[@class="evaluation_review"]/a')
            driver.execute_script("arguments[0].click();", another_reviews)
            time.sleep(2)
        except:
            break

    rates = driver.find_elements(By.XPATH, '//*[@id="mArticle"]/div[7]/div[3]/ul/li/div[2]/div/span/span')
    reviews = driver.find_elements(By.XPATH, '//*[@class="comment_info"]/p/span')
    ratess = []
    for i in range(0, len(rates)):
        rate = rates[i].get_attribute("style").replace("width:","").replace("%","").replace(";","").replace(" ","")
        rate = int(rate)/20
        ratess.append(rate)
    for rate, review in zip(ratess, reviews):
        row = [rate, review.text]
        series = pd.Series(row, index=df.columns)
        df = df.append(series, ignore_index=True)
    
driver.close()

df['y'] = df['score'].apply(lambda x: 1 if x > 3 else 0)
# print(df.shape)
# print(df.head(30))

def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub(' ',text)
    return result
df['review'] = df['review'].apply(lambda x: text_cleaning(x))
df = df[df['review'].str.len() > 0]
print(df.head(30))
print(len(df))

from konlpy.tag import Okt

def get_pos(x):
    tagger = Okt()
    pos = tagger.pos(x)
    pos = ['{}/{}'.format(word,tag) for word, tag in pos]
    return pos

result = get_pos(df['review'].values[0])
# print(result)

from sklearn.feature_extraction.text import CountVectorizer

index_vectorizer = CountVectorizer(tokenizer= lambda x: get_pos(x))
X = index_vectorizer.fit_transform(df['review'].tolist())
# print(X.shape)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_vectorizer = TfidfTransformer()
X = tfidf_vectorizer.fit_transform(X)

from sklearn.model_selection import train_test_split

y = df['y']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
# print(x_train.shape)
# print(x_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

lr = LogisticRegression(random_state=0)
lr.fit(x_train,y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

print("accuracy : %.2f" % accuracy_score(y_test, y_pred))
print("Precision : %.3f" % precision_score(y_test,y_pred))
print("Recall : %.3f" % recall_score(y_test,y_pred))
print("F1 : %.3f" % f1_score(y_test,y_pred))

from sklearn.metrics import confusion_matrix

confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

print(df['y'].value_counts())

from sklearn.metrics import roc_curve, roc_auc_score

# AUC를 계산합니다.
false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred_probability)
roc_auc = roc_auc_score(y_test, y_pred_probability)
print("AUC : %.3f" % roc_auc)

# ROC curve 그래프를 출력합니다.
# plt.rcParams['figure.figsize'] = [5, 4]
# plt.plot(false_positive_rate, true_positive_rate, label='ROC curve (area = %0.3f)' % roc_auc, 
#          color='red', linewidth=4.0)
# plt.plot([0, 1], [0, 1], 'k--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.0])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC curve of Logistic regression')
# plt.legend(loc="lower right")

# plt.show()

lr = LogisticRegression(random_state=0)
lr.fit(x_train,y_train)
y_pred = lr.predict(x_test)
y_pred_probability = lr.predict_proba(x_test)[:,1]

print("accuracy : %.2f" % accuracy_score(y_test, y_pred))
print("Precision : %.3f" % precision_score(y_test,y_pred))
print("Recall : %.3f" % recall_score(y_test,y_pred))
print("F1 : %.3f" % f1_score(y_test,y_pred))

confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
print(confmat)

plt.rcParams['figure.figsize'] = [10, 8]
plt.bar(range(len(lr.coef_[0])), lr.coef_[0])
plt.show()
print(sorted(((value, index) for index, value in enumerate(lr.coef_[0])), reverse=True)[:5])
print(sorted(((value, index) for index, value in enumerate(lr.coef_[0])), reverse=True)[-5:])

coef_pos_index = sorted(((value, index) for index, value in enumerate(lr.coef_[0])), reverse=True)
invert_index_vectorizer = {v:k for k, v in index_vectorizer.vocabulary_.items()}

print(str(invert_index_vectorizer)[:100]+'..')

for coef in coef_pos_index[:20]:
    print(invert_index_vectorizer[coef[1]], coef[0])

for coef in coef_pos_index[-20:]:
    print(invert_index_vectorizer[coef[1]], coef[0])

noun_list = []
adjective_list = []

# 명사, 형용사별로 계수가 높은 상위 10개의 형태소를 추출합니다. 이는 리뷰에 긍정적인 영향을 주는 명사와 형용사를 순위별로 살펴보는 것이 됩니다.
for coef in coef_pos_index[:100]:
    pos_category = invert_index_vectorizer[coef[1]].split("/")[1]
    if pos_category == "Noun":
        noun_list.append((invert_index_vectorizer[coef[1]], coef[0]))
    elif pos_category == "Adjective":
        adjective_list.append((invert_index_vectorizer[coef[1]], coef[0]))

print(noun_list[:10])
print(adjective_list[:10])