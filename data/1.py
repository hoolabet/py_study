import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "python-data-analysis-master/data/chipotle.tsv"

chipo = pd.read_csv(file_path, sep="\t")

# print(chipo.shape)
# print("-"*20)
# print(chipo.info())

# print(chipo.head(10))

# print(chipo.columns)
# print("-"*20)
# print(chipo.index)

# chipo["order_id"] = chipo["order_id"].astype(str)
# print(chipo.describe())

# print(len(chipo["order_id"].unique()))
# print(len(chipo["item_name"].unique()))

# item_count = chipo["item_name"].value_counts()[:10]

# for idx, (v,c) in enumerate(item_count.items(),1): # iteritems => items()
#     print(f"Top {idx} : {v} {c}")

# order_count = chipo.groupby("item_name")["order_id"].count()
# print(order_count[:10])

# item_quantity = chipo.groupby("item_name")["quantity"].sum()
# for idx, (v,c) in enumerate(item_quantity.items(),1):
#     print((f"{idx} : {v} {c}"))

# item_name_list = item_quantity.index.tolist()

# x_pos = np.arange(len(item_name_list))

# order_cnt = item_quantity.values.tolist()

# plt.bar(x_pos, order_cnt, align="center")
# plt.ylabel("ordered_item_count")
# plt.title("Distribution of all ordered item")

# plt.show()

chipo["item_price"] = chipo["item_price"].apply(lambda x : float(x[1:])) # "$" 제거, type object => float
chipo["order_id"] = chipo["order_id"].astype(str)

print(chipo.groupby("order_id")["item_price"].sum().mean())

chipo_orderid_group = chipo.groupby("order_id").sum(numeric_only=True)
results = chipo_orderid_group[chipo_orderid_group.item_price >= 10]
print(results[:10])
print(results.index.values)