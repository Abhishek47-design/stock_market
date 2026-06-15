import pandas as pd 

df = pd.read_json('data/raw/stocks.json', lines=True)
print(df.head())
print(df.shape)