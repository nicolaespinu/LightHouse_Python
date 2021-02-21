# Day Four: for loops
# Dot's now happily mapped out exactly what supplies they'll need to make the repairs to their new rural abode.
# They're nearly breathless with anticipation, thinking about how incredible it's going to look! But first,
# they need to buy the paint and wood. There's so much Dot needs to purchase, they're unsure - should
# they buy the items at normal retail value, or wholesale?


# Tutorial
# In this challenge, you'll need to use a for loop to reach the answer. In programming, a loop is a block of code that's executed repeatedly, either for a set number of times, or until a certain condition is met. A for loop is a loop that is executed for a set number of times, iterated over the number of items in a sequence. To learn more about for loops, read this article.
#
# lst = [1,2,3,4,5]
#
#
# for i in range(len(lst)):
#     '''insert code'''
# In the above code, the range() function creates a sequence of numbers, and the len() function outputs
# the length of a list.
#
# Challenge:
# Dot needs to purchase:
#
# 600 planks of Oak Wood
# 150 liters of Blue Paint
# 15 liters of White Paint
# 165 liters of Paint Finish
# Use a loop to determine the price Dot would pay for purchasing supplies at the retail price.
# Based on that calculation, which itmes should Dot buy at retail vs. wholesale?
#
# Note: Assume the wholesale price covers all the supply Dot needs for each item,
# whereas the retail price is per single unit.

item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']

amount_list = [600,150,15,165]

wholesale_price_list = [7000, 1000, 1000, 800]

retail_price = [12.99, 8.99, 9.99, 3.99]
# Solution
full_price = []

for i in range(len(item_list)):
    total_price = amount_list[i] * retail_price[i]
    full_price.append(total_price)

print(full_price);
