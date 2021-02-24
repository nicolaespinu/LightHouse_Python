# Challenge 8
# After playing around with the functions above, you can start helping Dot figure out when the best time
# to rent a cow might be. With this dataset, you can take a look at how cows produce milk over time.
#
# Answer the following questions for Dot:
#
# At what year and month did company x produce the most milk?
# At what year and month did company x produce the least milk?
# Stretch
#
# Stretch questions are not required to be completed for the challenge, but you can test your skills
# with more advanced challenges.
#
# Which year produced the most milk?
# import the pandas plugin
import pandas as pd

df = pd.read_csv('milk.csv');
print(df.describe());

maxim = df['Monthly milk production: pounds per cow'].idxmax();
minim = df['Monthly milk production: pounds per cow'].idxmin();

print('The maxim quantity of milk is: ', df.loc[maxim][1], ' is on  date ', df.loc[maxim][0]);
print('The minim quantity of milk is: ', df.loc[minim][1], ' is on  date ', df.loc[minim][0]);
