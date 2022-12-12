import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "python-data-analysis-master/data/drinks.csv"
drinks = pd.read_csv(file_path)
drinks["continent"] = drinks["continent"].fillna("OT")

drinks_wine_servings_mean = drinks.groupby("continent")["wine_servings"].mean()

print(drinks_wine_servings_mean)