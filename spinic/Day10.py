# Challenge
#
# Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:
#
# Total Milk Production
# Total Revenue
# How much revenue did the cow farm make in the year 2020?
import pandas as pd

df = pd.read_csv('milk_32.csv')
df = df.drop(columns = ['Unnamed: 0'])

#rename this because its too long "inplace=True" so it changes actual column
df.rename(columns={"Monthly milk production: pounds per cow":"Milk/Cow"}, inplace=True)

#maths to fill columns
df['Total Milk Production'] = df['Milk/Cow'] * df['Number of Cows']
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']

#make new column for year
df['Year'] = df['Month'].str[:2]

#Add df['Total Revenue'] WHERE  df['Year'] == 20
profit = df['Total Revenue'][df['Year'] == '20'].sum()
print("Total Revenue for 2020: ${}".format(profit))