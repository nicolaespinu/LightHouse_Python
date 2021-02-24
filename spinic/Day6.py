# Challenge:
# There are many holes in the living room's ceiling that desperately need to be fixed. Dot's measured them, and in total there are about 100. They need to figure out how much does it cost to fix all of the holes. Differently sized holes will require differently sized patches to fix them.
#
# Size of Hole	Cost to Fix
# Small (less than 20 mm)	$1.30
# Medium (above or equal to 20 mm AND less than 70mm)	$1.60
# Large (above or equal to 70 mm)	$2.10
# Dot needs you to look at the measurements and figure out the answers to the following questions:
#
# What is the average sized hole?
# What is the average cost to fix a hole?
# What is the total cost of fixing all of the holes?
#
# Note: Use a for loop and an if else statement to answer Q3.
# Stretch Question:
#
# Stretch Questions are not required to be completed to finish the challenge but are recommended
# to further develop your skills.
#
# What is the maximum sized hole?
# What is the minimum sized hole?
import random

import pandas as pd
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

series = pd.Series(hole_sizes)
print(f"Average sized hole {series.mean()}")
hole_prices = []
for i in range(len(hole_sizes)):
    if hole_sizes[i] < 20:
        hole_prices.append(1.30)
    elif hole_sizes[i] >= 20 and hole_sizes[i] < 70:
        hole_prices.append(1.6)
    else:
        hole_prices.append(2.10)
price_series = pd.Series(hole_prices)
print(f"Average cost to fix a hole is {price_series.mean()}")
print(f"Total cost to fix all holes is {sum(hole_prices)}")
print(f"Max size hole is {series.min()}")
print(f"Min size hole is {series.max()}")