# Challenge
# What type of distribution does the column avg_time have?
#
# Do games that have a great avg_rating have longer play times?
#
# Note: For question 2, filter out games that have are above the avg_rating of 9.0.
#
# Stretch
#
# As an optional bonus question, try answering:
#
# What type of distribution does weight have?
#
# What happens to the median and mean of a skewed distribution?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('boardgames.csv')
df.head(3)

new_df = df[df['avg_rating'] >= 9]
plt.figure()
plt.hist(df['avg_time'], bins=40, range=(0, 5000))
plt.show()

print(df['avg_time'].min())
print(df['avg_time'].max())

print(df['avg_time'].count())
print(new_df['avg_time'].count())

print(4999 / 40)


