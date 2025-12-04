#Day 25: 30 Days of python programming

import pandas as pd

df = pd.read_csv('/Users/alejandrobernardodavila/Desktop/EstructuraDirectorio/30DaysOfPython/hacker_news.csv')
df.info()
print(df.head())
print(df.tail())
print(df.columns)
print(df['title'])
print(df[df['title'].str.contains('python', case=False)])
print(df[df['title'].str.contains('JavaScript', case=False)])
print(df.describe().T)
