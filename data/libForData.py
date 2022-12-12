# %matplotlib inline
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

# names = ["Bob", "Jessica", "Mary", "John", "Mel"]
# births = [968, 155, 77, 578, 973]
# custom = [1, 5, 25, 13, 23232]

# BabyDataSet = list(zip(names,births))
# df = pd.DataFrame(data = BabyDataSet, columns = ["Names", "Births"], index=["a","b","c","d","e"])

# y = df["Births"]
# x = df["Names"]

# plt.bar(x, y)
# plt.xlabel("Names")
# plt.ylabel("Births")
# plt.title("Bar plot")
# plt.show()

np.random.seed(19920613)

x = np.arange(0.0, 100.0, 5.0)
y = (x * 1.5) + np.random.rand(20) * 50

plt.scatter(x, y, c="black", alpha=1, label="scatter point")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc="upper left")
plt.title("Scatter plot")
plt.show()

