import pandas as pd
# Pandas is used to analyze data
df=pd.read_csv("gov_finance.csv")

print("----Dataset Description-----")
print(df.describe())

print("----Dataset type-----")
print(type(df))

print("----Head Data-----")
print(df.head())

print("----Tail Data-----")
print(df.tail())


