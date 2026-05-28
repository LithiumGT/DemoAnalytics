import pandas as pd

df = pd.read_csv("sales.csv")

# Считаем сумму по колонке price для каждой страны
country_revenue = df.groupby("country")["price"].sum()

print(country_revenue)