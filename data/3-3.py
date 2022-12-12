import time
import operator

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

rating_file_path = "python-data-analysis-master/data/ml-1m/ratings.dat"
movie_file_path = "python-data-analysis-master/data/ml-1m/movies.dat"
user_file_path = "python-data-analysis-master/data/ml-1m/users.dat"

rating_data = pd.io.parsers.read_csv(rating_file_path, encoding = "ISO-8859-1", engine='python',
                                        names=['user_id', 'movie_id', 'rating', 'time'],
                                        delimiter='::'
                                    )
movie_data = pd.io.parsers.read_csv(movie_file_path, encoding = "ISO-8859-1", engine='python',
                                        names=['movie_id', 'title', 'genre'],
                                        delimiter='::'
                                    )                                
user_data = pd.io.parsers.read_csv(user_file_path, encoding = "ISO-8859-1", engine='python',
                                        names=['user_id', 'gender', 'age', 'occupation', 'zipcode'],
                                        delimiter='::'
                                    )                                    

# print(rating_data.head())
# print(movie_data.head())
# print(user_data.head())

# print(f"total number of movie in data : {len(movie_data['movie_id'].unique())}")
# movie_data['year'] = movie_data['title'].apply(lambda x : x[-5:-1])
# print(movie_data['year'].value_counts().head(10))

# unique_genre_dict = {}
# for i, r in movie_data.iterrows():
#     genre_combination = r['genre']
#     parsed_genre = genre_combination.split('|')

#     for genre in parsed_genre:
#         if genre in unique_genre_dict:
#             unique_genre_dict[genre] += 1
#         else:
#             unique_genre_dict[genre] = 1

# plt.rcParams['figure.figsize'] = [10, 8]
# plt.bar(list(unique_genre_dict.keys()), list(unique_genre_dict.values()), alpha=0.8)
# plt.title('Popular genre in movies')
# plt.xlabel('Count of Genre', fontsize=2)
# plt.ylabel('Genre', fontsize=2)
# plt.show()

# movie_rate_count = rating_data.groupby('movie_id')['rating'].count().values
# plt.rcParams['figure.figsize'] = [8, 8]
# fig = plt.hist(movie_rate_count, bins=200)
# plt.ylabel('Count', fontsize=12)
# plt.xlabel('Movie`s rated count', fontsize=12)
# print(f"total number of movie in data : {len(movie_data['movie_id'].unique())}")
# print(f"total number of movie rated below 100 : {len(movie_rate_count[movie_rate_count < 100])}")
# plt.show()

# movie_grouped_rating_info = rating_data.groupby('movie_id')['rating'].agg(['count','mean'])
# movie_grouped_rating_info.columns = ['rated_count', 'rating_mean']
# plt.hist(movie_grouped_rating_info['rating_mean'], bins=150)
# plt.show()

# rating_table = rating_data[['user_id', 'movie_id', 'rating']].set_index(['user_id', 'movie_id']).unstack()

# plt.rcParams['figure.figsize'] = [10, 10]
# plt.imshow(rating_table)
# plt.grid(False)
# plt.xlabel("Movie")
# plt.ylabel("User")
# plt.title("User-Movie Matrix")
# plt.show()

from surprise import SVD, Dataset, Reader, accuracy
from surprise.model_selection import train_test_split

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(rating_data[['user_id', 'movie_id', 'rating']], reader)
train_data = data.build_full_trainset()

train_start = time.time()
model = SVD(n_factors=8,
            lr_all=0.005,
            reg_all=0.02,
            n_epochs=100)
model.fit(train_data)
train_end = time.time()
# print(f"training time of model : {train_end - train_start} seconds")

target_user_id = 4
target_user_data = rating_data[rating_data['user_id'] == target_user_id]
# print(target_user_data.head(5))

target_user_movie_rating_dict = {}

for i, r in target_user_data.iterrows():
    movie_id = r["movie_id"]
    target_user_movie_rating_dict[movie_id] = r["rating"]

# print(target_user_movie_rating_dict)

# test_data = []
# for i, r in movie_data.iterrows():
#     movie_id = r['movie_id']
#     rating = 0
#     if movie_id in target_user_movie_rating_dict:
#         continue
#     test_data.append((target_user_id, movie_id, rating))

# target_user_predictions = model.test(test_data)

# def get_user_predicted_ratings(predictions, user_id, user_history):
#     target_user_movie_predict_dict = {}
#     for uid, mid, rating, predicted_rating, _ in predictions:
#         if user_id == uid:
#             if mid not in user_history:
#                 target_user_movie_predict_dict[mid] = predicted_rating
#     return target_user_movie_predict_dict

# target_user_movie_predict_dict = get_user_predicted_ratings(predictions=target_user_predictions,
#                                                             user_id=target_user_id,
#                                                             user_history=target_user_movie_rating_dict)

# target_user_top10_predicted = sorted(target_user_movie_predict_dict.items(), key=operator.itemgetter(1), reverse=True)[:10]
# print(target_user_top10_predicted)

# movie_dict = {}
# for i, r in movie_data.iterrows():
#     movie_id = r['movie_id']
#     movie_title = r['title']
#     movie_dict[movie_id] = movie_title

# for predicted in target_user_top10_predicted:
#     movie_id = predicted[0]
#     predicted_rating = predicted[1]
#     print(movie_dict[movie_id], ":", predicted_rating)

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(rating_data[['user_id', 'movie_id', 'rating']], reader)
train_data, test_data = train_test_split(data, test_size=0.2)

train_start = time.time()
model = SVD(n_factors=8,
            lr_all=0.005,
            reg_all=0.02,
            n_epochs=100)
model.fit(train_data)
train_end = time.time()
print(f"training time of model : {train_end - train_start} seconds")

# predictions = model.test(test_data)
# accuracy.rmse(predictions=predictions)

test_data = []
for i, r in movie_data.iterrows():
    movie_id = r['movie_id']
    if movie_id in target_user_movie_rating_dict:
        rating = target_user_movie_rating_dict[movie_id]
        test_data.append((target_user_id, movie_id, rating))

target_user_predictions = model.test(test_data)

def get_user_predicted_ratings(predictions, user_id, user_history):
    target_user_movie_predict_dict = {}
    for uid, mid, rating, predicted_rating, _ in predictions:
        if user_id == uid:
            if mid not in user_history:
                target_user_movie_predict_dict[mid] = predicted_rating
    return target_user_movie_predict_dict

target_user_movie_predict_dict = get_user_predicted_ratings(predictions=target_user_predictions,
                                                            user_id=target_user_id,
                                                            user_history=target_user_movie_rating_dict)

print(target_user_movie_predict_dict)