# Challenge
# Examining the numbers, Dot understands that the prices of both conventional and organic avocados rise
# and fall frequently. No matter how they grow the avocados, they don't want to sell them for less than $2.
#
# Looking at recent years, Dot needs you to help them find: in which year or years did both conventional
# and organic avocados have had average prices above $2?
import pandas as pd

df = pd.read_csv('avocado.csv', index_col = 0)
df.head()
df = df[df['AveragePrice'] >= 2]
df.head()
print(df.groupby(['year', 'type']).min())
