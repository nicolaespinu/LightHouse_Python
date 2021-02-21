# Tutorial:
# Numbers
# There are two main numeric data types in Python, integers and float.
# The integer data types refer to whole numbers, while float data types refer to any numeric value that isn't a whole, like a fraction or a decimal.
# In Python as well as any other programming language, there are a variety of math operations you can use to do basic arithmetic.
# To learn more about numbers in Python, take a look at these articles here and here.
# In Python, lists are a type of variable that can be sequenced. Lists can contain many items that can be indexed by integers, with items being kept separate by the ','.
# list = [] #lists are called using the square brackets
# list_of_int = [1,2,3,4,5] #list of integers
# list_of_string = ['string1','string2', 'string3'] #list of strings
# list_of_anything = [1, 'string', 3.2] #list with an integer, string, and float.
# To learn more about lists, check out this article here.
# Challenge
# Dot has a few lists you can use as reference: their grocery list, the prices they used to pay in the city,
# and the prices for the rural grocer.
# What is the price difference between groceries in the city vs. groceries in the country,
# as a percentage of country prices?
# Note: The index position for each item is consistent across all three lists.
# Grocery List (19 items)
grocery_list = ['Bananas', 'Clementines', 'Baguette', 'Oat Milk', 'Olive Oil', 'Coffee Beans',
                'Chocolate Bar', 'Brocolli', 'Eggplant', 'Chickpeas', 'Lentils', 'Tomatoes',
                'Pasta', 'Rice', 'Yogurt', 'Blueberries', 'Onions', 'Garlic', 'Truffles']

# City Price
city_price = [6.49, 4.99, 4.39, 4.29, 11.99, 17.99,
              3.49, 3.99, 1.10, 1.99, 2.99, 4.68,
              1.59, 8.99, 3.49, 6.99, 2.99, 1.98, 14.99]

# Country Price
country_price = [4.49, 4.12, 3.42, 6.99, 7.99, 14.99,
                 2.99, 2.49, 0.99, 1.49, 2.49, 1.99,
                 1.59, 6.99, 3.89, 4.99, 1.69, 1.87, 11.49]

# print(sum(city_price));
# print(sum(country_price));
city_s = sum(city_price);
country_s = sum(country_price);
r = (city_s - country_s);

print(r / country_s);
