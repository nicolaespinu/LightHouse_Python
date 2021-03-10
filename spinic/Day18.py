# Challenge¶
# What are the top 5 boardgame categories in this dataset that are not targeted for young children?
# Note: For the question above, use a filter to acquire boardgames with an inteded age of 13+, there is an age
# column in our dataset.
# Which categories of boardgames that are not targeted for young children are the same compared
# to the top 5 boardgames categories in the overall dataset?

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('boardgames.csv')
df.head(2)

df[df['age'] >= 13].groupby(df['category']).count().sort_values(by='rank', ascending=False).head()

df.groupby(df['category']).count().sort_values(by='rank', ascending=False).head()