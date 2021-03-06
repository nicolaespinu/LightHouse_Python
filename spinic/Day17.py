# Challenge
# Help Dot by answering the following questions using a bar plot:
#
# What are the top 5 rated books in the dataset?
#
# What are the top 5 books with the highest average rating?
#
# Note: Filter out books that have low ratings_count, for question 2 filter out books with a ratings_count less than the mean.
#
# Stretch
#
# As an optional bonus question, try answering this as well:
#
# What are the top 5 authours with the most books in the dataset?

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("books.csv")

df.head(2)

rated_df = df.sort_values(by='ratings_count', ascending=False).head()

plt.barh(y=rated_df['title'], width=rated_df['ratings_count'])
plt.show()

avg_df = df[df['ratings_count'] > df['ratings_count'].mean()]
avg_df = avg_df.sort_values(by='average_rating', ascending=False).head()
avg_df

plt.barh(y=avg_df['title'], width=avg_df['average_rating'])
plt.show()