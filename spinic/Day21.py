# Challenge
# Dot wants to play retro video games with all their new friends! Help them figure out which games would be best.
# Questions:
# What is the correlation coefficient between Critic_Score and User_Score?
# Note: You may have to clean some of the columns and fill it with the median value (if numerical).
# Plot the top 5 best selling games released before the year 2000.
# Note: Use Global_Sales
# Create a new column called Aggregate_Score, which returns the proportional average between Critic Score and User_Score based on Critic_Count and User_Count. Plot a horizontal bar chart of the top 5 highest rated games by Aggregate_Score, not published by Nintendo before the year 2000. From this bar chart, what is the highest rated game by Aggregate_Score?
# Note: Critic_Count should be filled with the mean. User_Count should be filled with the median.
# Stretch:
# Don't stop at the above challenges, be inquisitive of your given dataset, dive deeper, and share your insights on the forum. For your reference, the dataset used in today's challenge can be downloaded for free from Kaggle.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('video_games.csv')
df.head(2)

critic_score_median = df['Critic_Score'].median()
user_score_median = df['User_Score'].median()
user_score_median

df['Critic_Score'] = df['Critic_Score'].fillna(value=critic_score_median)
df['User_Score'] = df['User_Score'].fillna(value=user_score_median)
df[['Critic_Score','User_Score']].corr()

global_sales_df = df[df['Year_of_Release'] < 2000]
global_sales_df = global_sales_df.sort_values(by='Global_Sales', ascending = False).head()

plt.figure()
plt.title('top 5 best selling games released before the year 2000')
plt.xlabel('Global_Sales')
plt.barh(y=global_sales_df['Name'], width = global_sales_df['Global_Sales'])
print(plt.show())
