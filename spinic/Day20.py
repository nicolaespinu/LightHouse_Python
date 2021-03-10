# Challenge
# Play around with the scatterplot and test out different correlations between the numerical categories in the dataset. Then, help Dot by answering these questions:
#
# What kind of correlation is there between the weight and avg_rating?
#
# What is the correlation coefficient between the two columns?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('boardgames.csv')
df.head(3)

plt.figure()
plt.scatter(x = df['weight'], y = df['avg_rating'])
plt.show()
plt.figure()

plt.title('Correlation between weight and avg_rating')
plt.xlabel('Weight')
plt.ylabel('Average Rating ')
plt.scatter(x = df['weight'], y = df['avg_rating'])
plt.show()

print(df[['weight', 'avg_rating']].corr())
