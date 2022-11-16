import pandas as pd

names = ["Bob", "Jessica", "Mary", "John", "Mel"]
births = [968, 155, 77, 578, 973]
custom = [1, 5, 25, 13, 23232]

BabyDataSet = list(zip(names,births))
df = pd.DataFrame(data = BabyDataSet, columns = ["Names", "Births"], index=["a","b","c","d","e"])
print(df)
print(df.head())
print(df.dtypes)
print(df.index)
print(df.columns)
print(df[df["Births"] > 200])
print(df["Births"].mean())