# Challenge
# Use the pandas sort function and the pandas filter function from the previous challenge to answer these questions:
#
# Which wines had a quality of 8 or higher and a residual sugar level above 5?
# How many wines in total had a quality of 8 and 7 and a citric acid level below 0.4?
# Note: Use the index positions of the wines as the wine names.
import pandas as pd
wine_df = pd.read_csv('winequality-red.csv')
wine_df
# wine_df = wine_df[wine_df['quality'] >= 8]
# wine_df = wine_df[wine_df['residual sugar'] > 5]
# wine_df
wine_df.sort_values(by=['quality', 'residual sugar'], ascending = False)
wine_df.sort_values(by=['citric acid','quality'], ascending = False)
wine_df
wine_df = wine_df[wine_df['citric acid'] < 0.4]
wine_df = wine_df[wine_df['quality'] >= 7]
wine_df