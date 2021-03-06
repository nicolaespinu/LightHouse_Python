# Challenge
# Create a boxplot to answer the following questions:
#
# How many books have over 4000 pages?
#
# Note: Do not use a fitler, use a boxplot.
#
# What are the average ratings for books that have over 4000 pages?
#
# Note: You can use a filter for question 2.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("books.csv")
df.columns

#1
plt.figure()
plt.boxplot(df['num_pages'], vert=False)
plt.show()
#2
page_filter = df['num_pages'] > 4000
x = df[page_filter]
x.groupby('average_rating').mean()