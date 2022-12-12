import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "python-data-analysis-master/data/drinks.csv"
drinks = pd.read_csv(file_path)

# print(drinks.info())
# print(drinks.head(10))

# corr = drinks[["beer_servings", "wine_servings"]].corr(method="pearson")
# print(corr)

# cols = ["beer_servings", "spirit_servings", "wine_servings", "total_litres_of_pure_alcohol"]
# corr = drinks[cols].corr(method="pearson")
# print(corr)

# cols_view = ["beer", "spirit", "wine", "alcohol"]
# sns.set(font_scale = 1.5)
# hm = sns.heatmap(corr.values,
#         cbar=True,
#         annot=True,
#         square=True,
#         fmt=".2f",
#         annot_kws={"size": 15},
#         yticklabels=cols_view,
#         xticklabels=cols_view
# )
# plt.tight_layout()
# plt.show()

# sns.set(style="whitegrid", context="notebook")
# sns.pairplot(drinks[cols], height=2.5)
# plt.show()

drinks["continent"] = drinks["continent"].fillna("OT")
# print(drinks.head(20))

# labels = drinks["continent"].value_counts().index.tolist()
# fracs1 = drinks["continent"].value_counts().values.tolist()
# expload = (0,0,0,0.25,0,0)

# plt.pie(fracs1, explode=expload, labels=labels, autopct="%.0f%%", shadow=True)
# plt.title('null data to "OT"')
# plt.show()

result = drinks.groupby("continent").spirit_servings.agg(["mean","min","max","sum"])
# print(result.head(10))

total_mean = drinks.total_litres_of_pure_alcohol.mean()
continent_mean = drinks.groupby("continent")["total_litres_of_pure_alcohol"].mean()
# continent_over_mean = continent_mean[continent_mean >= total_mean]
# print(total_mean)
# print(continent_over_mean)

beer_continent = drinks.groupby("continent").beer_servings.mean().idxmax()
# print(beer_continent)

n_groups = len(result.index)
means = result["mean"].tolist()
mins = result["min"].tolist()
maxs = result["max"].tolist()
sums = result["sum"].tolist()

index = np.arange(n_groups)
bar_width = 0.1

# plt.bar(index, means, bar_width, color="r", label="Mean")
# plt.bar(index + bar_width, mins, bar_width, color="g", label="Min")
# plt.bar(index + bar_width * 2, maxs, bar_width, color="b", label="Max")
# plt.bar(index + bar_width * 3, sums, bar_width, color="y", label="Sum")

# plt.xticks(index, result.index.tolist())
# plt.legend()
# plt.show()

# continents = continent_mean.index.tolist()
# continents.append("mean")
# x_pos = np.arange(len(continents))
# alcohol = continent_mean.tolist()
# alcohol.append(total_mean)

# bar_list = plt.bar(x_pos, alcohol, align="center", alpha=0.5)
# bar_list[len(continents) - 1].set_color("r")
# plt.plot([0, 6], [total_mean, total_mean], "--m")
# plt.xticks(x_pos, continents)

# plt.ylabel("total_litres_of_pure_alcohol")
# plt.title("total_litres_of_pure_alcohol by Continent")

# plt.show()

# beer_group = drinks.groupby("continent")["beer_servings"].sum()
# continents = beer_group.index.tolist()
# y_pos = np.arange(len(continents))
# alcohol = beer_group.tolist()

# bar_list = plt.bar(y_pos, alcohol, align="center", alpha=0.5)
# bar_list[continents.index("EU")].set_color("r")
# plt.xticks(y_pos,continents)
# plt.ylabel("beer_servings")
# plt.title("beer_servings by Continent")

# plt.show()

africa = drinks.loc[drinks["continent"] == "AF"]
europe = drinks.loc[drinks["continent"] == "EU"]

from scipy import stats

tTestResult = stats.ttest_ind(africa["beer_servings"], europe["beer_servings"])
tTestResultDiffVar = stats.ttest_ind(africa["beer_servings"], europe["beer_servings"], equal_var=False)

# print("The t-statistic and p-value assuming equal variances is %.3f and %.3f." % tTestResult)
# print("The t-statistic and p-value not assuming equal variances is %.3f and %.3f." % tTestResultDiffVar)

drinks["total_servings"] = drinks["beer_servings"] + drinks["wine_servings"] + drinks["spirit_servings"]
drinks["alcohol_rate"] = drinks["total_litres_of_pure_alcohol"] / drinks["total_servings"]
drinks["alcohol_rate"] = drinks["alcohol_rate"].fillna(0)

country_with_rank = drinks[["country", "alcohol_rate"]]
country_with_rank = country_with_rank.sort_values(by=["alcohol_rate"], ascending=0)
print(country_with_rank.head(5))

country_list = country_with_rank.country.tolist()
x_pos = np.arange(len(country_list))
rank = country_with_rank.alcohol_rate.tolist()

bar_list = plt.bar(x_pos,rank)
bar_list[country_list.index("South Korea")].set_color("r")
plt.ylabel("alcohol rate")
plt.title("liquor drink rank bt country")
plt.axis([0, 200, 0, 0.3])

korea_rank = country_list.index("South Korea")
korea_alc_rate = country_with_rank[country_with_rank["country"] == "South Korea"]["alcohol_rate"].values[0]

plt.annotate("South Korea : "+str(korea_rank + 1),
    xy=(korea_rank,korea_alc_rate),
    xytext=(korea_rank + 10, korea_alc_rate + 0.05),
    arrowprops=dict(facecolor="red", shrink=0.05))

plt.show()