# Challenge
# Dot's neighbour said that he only likes wine from Stellenbosch, Bordeaux, and the Okanagan Valley,
# and that the sulfates can't be that high. The problem is, Dot can't really afford to spend tons
# of money on the wine. Dot's conditions for searching for wine are:
#
# Sulfates cannot be higher than 0.6.
# The price has to be less than $20.
# Use the above conditions to filter the data for questions 2 and 3 below.
#
# Questions:
#
#  1. Where is Stellenbosch, anyway? How many wines from Stellenbosch are there in the entire dataset?
#  2. After filtering with the 2 conditions, what is the average price of wine from the Bordeaux region?
#  3. After filtering with the 2 conditions, what is the least expensive wine that's of the highest quality
#     from the Okanagan Valley?
#
#  Stretch Question:
# What is the average price of wine from Stellenbosch, according to the entire unfiltered dataset?
# Note: Check the dataset to see if there are missing values; if there are, fill in missing values with the mean.



import pandas as pd
df = pd.read_csv('winequality-red_2.csv')
df = df.drop(columns = ['Unnamed: 0'])

df.head()
print('Q1  of wines from Stellenbosch:',df[df['region'].str.contains('Stellenbosch')].shape[0])

filterDF = df[(df['sulphates']<=0.6) & (df['price']<20)]
print("Q2 avg price of wines from Bordeaux: ",filterDF[filterDF['region']=='Bordeaux']['price'].mean())

print(filterDF[filterDF['region'].str.contains('Okanagan Valley')].sort_values(['quality','price'],ascending=[False,True]))

# 1. 35 Wines
# 2 .$11.30
# 3. Wine 1025