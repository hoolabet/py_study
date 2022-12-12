import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_train = pd.read_csv("python-data-analysis-master/data/titanic_train.csv")
df_test = pd.read_csv("python-data-analysis-master/data/titanic_test.csv")

df_train = df_train.drop(['name', 'ticket', 'body', 'cabin', 'home.dest'], axis=1)
df_test = df_test.drop(['name', 'ticket', 'body', 'cabin', 'home.dest'], axis=1)

# print(df_train['survived'].value_counts())
# df_train['survived'].value_counts().plot.bar()
# plt.show()

# print(df_train['pclass'].value_counts())
# ax = sns.countplot(x='pclass', hue='survived', data=df_train)
# plt.show()

from scipy import stats

def valid_features(df, col_name, distribution_check=True):
    g = sns.FacetGrid(df, col='survived')
    g.map(plt.hist, col_name, bins=30)
    plt.show()

    titanic_survived = df[df['survived'] == 1]
    titanic_survived_static = np.array(titanic_survived[col_name])
    print("data std is", '%.2f' % np.std(titanic_survived_static))
    titanic_n_survived = df[df['survived'] == 0]
    titanic_n_survived_static = np.array(titanic_n_survived[col_name])
    print("data std is", '%.2f' % np.std(titanic_n_survived_static))

    tTestResult = stats.ttest_ind(titanic_survived[col_name], titanic_n_survived[col_name])
    tTestResultDiffVar = stats.ttest_ind(titanic_survived[col_name], titanic_n_survived[col_name], equal_var=False)
    print("The t-statistic and p-value assuming equal variances is %.3f and %.3f." %tTestResult)
    print("The t-statistic and p-value not assuming equal variances is %.3f and %.3f." %tTestResultDiffVar)

    if distribution_check:
        print("The w-statistic and p-value in Survived %.3f and %.3f." %stats.shapiro(titanic_survived[col_name]))
        print("The w-statistic and p-value in Non-Survived %.3f and %.3f." %stats.shapiro(titanic_n_survived[col_name]))

# valid_features(df_train[df_train['age'] > 0], 'age', distribution_check=True)
# valid_features(df_train, 'sibsp', distribution_check=False)

# replace_mean = df_train[df_train['age'] > 0]['age'].mean()
# df_train['age'] = df_train['age'].fillna(replace_mean)
# df_test['age'] = df_test['age'].fillna(replace_mean)

# embarked_mode = df_train['embarked'].value_counts().index[0]
# df_train['embarked'] = df_train['embarked'].fillna(embarked_mode)
# df_test['embarked'] = df_test['embarked'].fillna(embarked_mode)

# whole_df = df_train.append(df_test)
# train_idx_num = len(df_train)

# whole_df_encoded = pd.get_dummies(whole_df)
# df_train = whole_df_encoded[:train_idx_num]
# df_test = whole_df_encoded[train_idx_num:]

# print(df_train.head())

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# x_train, y_train = df_train.loc[:, df_train.columns != 'survived'].values, df_train['survived'].values
# x_test, y_test = df_test.loc[:, df_test.columns != 'survived'].values, df_test['survived'].values

# lr = LogisticRegression(random_state=0)
# lr.fit(x_train,y_train)

# y_pred = lr.predict(x_test)
# y_pred_probabilty = lr.predict_proba(x_test)[:,1]

# print("accuracy : %.2f" % accuracy_score(y_test, y_pred))
# print("Precision : %.3f" % precision_score(y_test, y_pred))
# print("Recall : %.3f" % recall_score(y_test, y_pred))
# print("F1 : %.3f" % f1_score(y_test, y_pred))

from sklearn.metrics import confusion_matrix

# confmat = confusion_matrix(y_true=y_test, y_pred=y_pred)
# print(confmat)

from sklearn.metrics import roc_curve, roc_auc_score

# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred_probabilty)
# roc_auc = roc_auc_score(y_test, y_pred_probabilty)
# print("AUC : %.3f" % roc_auc)

# plt.rcParams['figure.figsize'] = [5,4]
# plt.plot(false_positive_rate, true_positive_rate, label='ROC curve (area = %0.3f)' % roc_auc, color='red', linewidth=4.0)
# plt.plot([0,1],[0,1], 'k--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.0])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC curve of Logistic regression')
# plt.legend(loc='lower right')
# plt.show()

from sklearn.tree import DecisionTreeClassifier

# dtc = DecisionTreeClassifier()
# dtc.fit(x_train, y_train)
# y_pred = dtc.predict(x_test)
# y_pred_probabilty = dtc.predict_proba(x_test)[:,1]

# print("accuracy : %.2f" % accuracy_score(y_test, y_pred))
# print("Precision : %.3f" % precision_score(y_test, y_pred))
# print("Recall : %.3f" % recall_score(y_test, y_pred))
# print("F1 : %.3f" % f1_score(y_test, y_pred))

# false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred_probabilty)
# roc_auc = roc_auc_score(y_test, y_pred_probabilty)
# print("AUC : %.3f" % roc_auc)

# plt.rcParams['figure.figsize'] = [5,4]
# plt.plot(false_positive_rate, true_positive_rate, label='ROC curve (area = %0.3f)' % roc_auc, color='red', linewidth=4.0)
# plt.plot([0,1],[0,1], 'k--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.0])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC curve of Logistic regression')
# plt.legend(loc='lower right')
# plt.show()

df_train = pd.read_csv("python-data-analysis-master/data/titanic_train.csv")
df_test = pd.read_csv("python-data-analysis-master/data/titanic_test.csv")

df_train = df_train.drop(['ticket', 'body', 'home.dest'], axis=1)
df_test = df_test.drop(['ticket', 'body', 'home.dest'], axis=1)

replace_mean = df_train[df_train['age'] > 0]['age'].mean()
df_train['age'] = df_train['age'].fillna(replace_mean)
df_test['age'] = df_test['age'].fillna(replace_mean)

embarked_mode = df_train['embarked'].value_counts().index[0]
df_train['embarked'] = df_train['embarked'].fillna(embarked_mode)
df_test['embarked'] = df_test['embarked'].fillna(embarked_mode)

whole_df = df_train.append(df_test)
train_idx_num = len(df_train)

# print(whole_df['cabin'].value_counts()[:10])

whole_df['cabin'] = whole_df['cabin'].fillna('X')
whole_df['cabin'] = whole_df['cabin'].apply(lambda x: x[0])
whole_df['cabin'] = whole_df['cabin'].replace({'G':'X', 'T':'X'})

# ax = sns.countplot(x='cabin', hue='survived', data=whole_df)
# plt.show()

name_grade = whole_df['name'].apply(lambda x : x.split(', ',1)[1].split('.')[0])
name_grade = name_grade.unique().tolist()
# print(name_grade)

grade_dict = {
    'A' : ['Rev', 'Col', 'Major', 'Dr', ' Capt', 'Sir'],
    'B' : ['Ms', 'Mme', 'Mrs', 'Dona'],
    'C' : ['Jonkheer', 'the Countess'],
    'D' : ['Mr', 'Don'],
    'E' : ['Master'],
    'F' : ['Miss', 'Mlle', 'Lady']
}

def give_grade(x):
    grade = x.split(', ',1)[1].split('.')[0]
    for k, v in grade_dict.items():
        for t in v:
            if grade == t:
                return k
    return 'G'

whole_df['name'] = whole_df['name'].apply(lambda x: give_grade(x))
# print(whole_df['name'].value_counts())

whole_df_encoded = pd.get_dummies(whole_df)
df_train = whole_df_encoded[:train_idx_num]
df_test = whole_df_encoded[train_idx_num:]
# print(df_train.head())

x_train, y_train = df_train.loc[:, df_train.columns != 'survived'].values, df_train['survived'].values
x_test, y_test = df_test.loc[:, df_test.columns != 'survived'].values, df_test['survived'].values

lr = LogisticRegression(random_state=0)
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)
y_pred_probabilty = lr.predict_proba(x_test)[:,1]

print("accuracy : %.2f" % accuracy_score(y_test, y_pred))
print("Precision : %.3f" % precision_score(y_test, y_pred))
print("Recall : %.3f" % recall_score(y_test, y_pred))
print("F1 : %.3f" % f1_score(y_test, y_pred))

false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, y_pred_probabilty)
roc_auc = roc_auc_score(y_test, y_pred_probabilty)
# print("AUC : %.3f" % roc_auc)

# plt.rcParams['figure.figsize'] = [5,4]
# plt.plot(false_positive_rate, true_positive_rate, label='ROC curve (area = %0.3f)' % roc_auc, color='red', linewidth=4.0)
# plt.plot([0,1],[0,1], 'k--')
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.0])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('ROC curve of Logistic regression')
# plt.legend(loc='lower right')
# plt.show()

cols = df_train.columns.tolist()
cols.remove('survived')
y_pos = np.arange(len(cols))

# plt.rcParams['figure.figsize'] = [5, 4]
# ax = plt.subplot()
# ax.barh(y_pos, lr.coef_[0], align='center', color='green', ecolor='black')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(cols)
# ax.invert_yaxis()
# ax.set_xlabel('Coef')
# ax.set_title('Each Feature`s Coef')

# plt.show()

from sklearn.model_selection import KFold

k = 5
cv = KFold(k, shuffle=True, random_state=0)
auc_history = []

for i, (train_data_row, test_data_row) in enumerate(cv.split(whole_df_encoded)):
    df_train = whole_df_encoded.iloc[train_data_row]
    df_test = whole_df_encoded.iloc[test_data_row]

    splited_x_train, splited_y_train = df_train.loc[:, df_train.columns != 'survived'].values, df_train['survived'].values
    splited_x_test, splited_y_test = df_test.loc[:, df_test.columns != 'survived'].values, df_test['survived'].values

    lr = LogisticRegression(random_state=0)
    lr.fit(splited_x_train, splited_y_train)
    y_pred = lr.predict(splited_x_test)
    y_pred_probabilty = lr.predict_proba(splited_x_test)[:,1]

    false_positive_rate, true_positive_rate, thresholds = roc_curve(splited_y_test, y_pred_probabilty)
    roc_auc = roc_auc_score(splited_y_test, y_pred_probabilty)
    auc_history.append(roc_auc)

# plt.xlabel('Each K-fold')
# plt.ylabel('AUC of splited test data')
# plt.plot(range(1, k+1), auc_history)
# plt.show()

import scikitplot as skplt
skplt.estimators.plot_learning_curve(lr,x_train,y_train)
plt.show()