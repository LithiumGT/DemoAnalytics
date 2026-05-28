import pandas as pd

df = pd.DataFrame(
   data={
       "price": [2_500_000, 4_200_000, 1_800_000],
       "available": [True, False, True],
       "brand": ["Lada", "Chery", "Kia"]
   },
   index=["Vesta", "Tiggo", "Rio"]
)
df.loc["Tiggo", "price"] = 5_000_000
print(df)
