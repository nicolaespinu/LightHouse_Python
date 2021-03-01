# Challenge
# Can Dot spin a profit as an avocado farmer?
# Examine the data to find the average cost of avocados in Albany in 2017.
import pandas as pd

df = pd.read_csv('avocado.csv', index_col = 0)
df.head()

df = df[df['year'] == 2017]
df = df[df['region'] == 'Albany']
df.head()

print(df.groupby(['year','region'])['AveragePrice'].mean())
print('Hello')