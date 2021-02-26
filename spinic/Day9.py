# Challenge
# Fill out the missing values in the monthly milk production column with the median, and fill out the number
# of cows column using the ffill method.
#
# After filling in the missing values with our new data, answer these questions for Dot, so they can figure
# out the value of having a cow year-round:
#
# What is the average for monthly milk production?
# What is the standard deviation for monthly milk production?
# What is the average number of cows used?
import pandas as pd

df = pd.read_csv('milk_2.csv')

milk = "Monthly milk production: pounds per cow"

median_milk = df[milk].median()
df[milk] = df[milk].fillna(value = median_milk)

df['Number of Cows'] = df['Number of Cows'].ffill(axis = 0)

print("Q1: The Average monthly milk prod is {}".format(round(df[milk].mean(), 4)))
print("Q2: The standard diviation for monthly milk prod is {}".format(round(df[milk].std(), 4)))
print("Q3: the average number of cows is {}".format(round(df['Number of Cows'].mean(), 4)))