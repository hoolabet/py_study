import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import statsmodels.api as sm

picher_file_path = "python-data-analysis-master/data/picher_stats_2017.csv"
batter_file_path = "python-data-analysis-master/data/batter_stats_2017.csv"
picher = pd.read_csv(picher_file_path)
batter = pd.read_csv(batter_file_path)

# print(picher.columns)
# print(picher.head())

# print(picher["연봉(2018)"].describe())
# plt.hist(picher["연봉(2018)"],bins=100)
# plt.show()

# plt.boxplot(picher["연봉(2018)"])
# plt.show()

picher_features_str = "승,패,세,홀드,블론,경기,선발,이닝,삼진/9,볼넷/9,홈런/9,BABIP,LOB%,ERA,RA9-WAR,FIP,kFIP,WAR,연봉(2018),연봉(2017)"
picher_features_list = picher_features_str.split(",")
picher_features_df = picher[picher_features_list]

def plot_hist_each_column(df):
    plt.rcParams["figure.figsize"] = [20, 16]
    plt.rcParams["font.family"] = "Malgun Gothic"
    plt.rcParams['axes.unicode_minus'] = False
    fig = plt.figure(1)

    for i in range(len(df.columns)):
        ax = fig.add_subplot(5, 5, i+1)
        plt.hist(df[df.columns[i]], bins=50)
        ax.set_title(df.columns[i])
    plt.show()

# plot_hist_each_column(picher_features_df)

pd.options.mode.chained_assignment = None

def standard_scaling(df, scale_columns):
    for col in scale_columns:
        series_mean = df[col].mean()
        series_std = df[col].std()
        df[col] = df[col].apply(lambda x: (x-series_mean) / series_std)
    return df

scale_columns = copy.copy(picher_features_list)
scale_columns.remove("연봉(2018)")

picher_df = standard_scaling(picher, scale_columns)
picher_df = picher_df.rename(columns={"연봉(2018)" : "y"})
# print(picher_df.head(5))

team_encoding = pd.get_dummies(picher_df["팀명"])
picher_df = picher_df.drop("팀명", axis=1)
picher_df = picher_df.join(team_encoding)
# print(team_encoding.head(5))

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

# X = picher_df[picher_df.columns.difference(["선수명", "y"])]
# Y = picher_df["y"]
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=19)

# lr = linear_model.LinearRegression()
# model = lr.fit(X_train, Y_train)

# print(lr.coef_)

# X_train = sm.add_constant(X_train)
# model = sm.OLS(Y_train,X_train).fit()
# print(model.summary())

# plt.rcParams["figure.figsize"] = [10, 8]
# plt.rcParams["font.family"] = "Malgun Gothic"
# plt.rcParams['axes.unicode_minus'] = False

# coefs = model.params.tolist()
# coefs_series = pd.Series(coefs)

# x_labels = model.params.index.tolist()

# ax = coefs_series.plot(kind="bar")
# ax.set_title("feature_coef_graph")
# ax.set_xlabel("x_features")
# ax.set_ylabel("coef")
# ax.set_xticklabels(x_labels)

# plt.show()

X = picher_df[picher_df.columns.difference(["선수명", "y"])]
Y = picher_df["y"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=19)

lr = linear_model.LinearRegression()
model = lr.fit(X_train, Y_train)

print(model.score(X_train, Y_train))
print(model.score(X_test, Y_test))

y_predictions = lr.predict(X_train)
print(sqrt(mean_squared_error(Y_train, y_predictions)))
y_predictions = lr.predict(X_test)
print(sqrt(mean_squared_error(Y_test, y_predictions)))

import seaborn as sns

corr = picher_df[scale_columns].corr(method="pearson")
show_cols = ['win','lose','save','hold','blon','match','start','inning','strike3','ball4','homerun','BABIP','LOB','ERA','RA9-WAR','FIP','kFIP','WAR','2017']

plt.rcParams["figure.figsize"] = [15, 10]
plt.rcParams["font.family"] = "Malgun Gothic"
sns.set(font_scale=1.0)
hm = sns.heatmap(
    corr.values,
    cbar=True,
    annot=True,
    square=True,
    fmt=".2f",
    annot_kws={"size": 15},
    yticklabels=show_cols,
    xticklabels=show_cols
)

# plt.tight_layout()
# plt.show()

from statsmodels.stats.outliers_influence import variance_inflation_factor

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif["features"] = X.columns
# print(vif.round(1))

X = picher_df[["FIP","WAR","볼넷/9","삼진/9","연봉(2017)"]]
lr = linear_model.LinearRegression()
predict_2018_salary = lr.predict(X)
picher_df["예측연봉(2018)"] = pd.Series(predict_2018_salary)

picher = pd.read_csv(picher_file_path)
picher = picher[["선수명","연봉(2017)"]]

result_df = picher_df.sort_values(by=["y"], ascending=False)
result_df.drop(["연봉(2017)"], axis=1, inplace=True, errors="ignore")
result_df = result_df.merge(picher, on=["선수명"], how="left")
result_df = result_df[["선수명","y","예측연봉(2018)","연봉(2017)"]]
result_df.columns = ["선수명","실제연봉(2018)","예측연봉(2018)","작년연봉(2017)"]

result_df = result_df[result_df["작년연봉(2017)"] != result_df["실제연봉(2018)"]]
result_df = result_df.reset_index()
result_df = result_df.iloc[:10, :]
print(result_df.head(10))