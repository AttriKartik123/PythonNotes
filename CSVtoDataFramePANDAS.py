# CSV to DataFrame
#You work for an airline, and your manager has asked you to do a competitive analysis and see how often passengers flying on other airlines are involuntarily bumped from their flights. You got a CSV file (airline_bumping.csv) from the Department of Transportation containing data on passengers that were involuntarily denied boarding in 2016 and 2017, but it doesn't have the exact numbers you want. In order to figure this out, you'll need to get the CSV into a pandas DataFrame and do some manipulation!

#pandas is imported for you as pd. "airline_bumping.csv" is in your working directory.
    

    #1Read the CSV file "airline_bumping.csv" and store it as a DataFrame called airline_bumping.
#Print the first few rows of airline_bumping.

# Read CSV as DataFrame called airline_bumping
airline_bumping = pd.read_csv("airline_bumping.csv")

# Take a look at the DataFrame
print(airline_bumping.head())




#2For each airline group, select the nb_bumped, and total_passengers columns, and calculate the sum (for both years). Store this as airline_totals.

import pandas as pd

# Load the CSV file into a DataFrame
airline_bumping = pd.read_csv("airline_bumping.csv")

# For each airline group, select the nb_bumped and total_passengers columns, and calculate the sum (for both years).
airline_totals = airline_bumping.groupby('airline')[['nb_bumped', 'total_passengers']].sum()

# Print the result
print(airline_totals)

#3Create a new column of airline_totals called bumps_per_10k, which is the number of passengers bumped per 10,000 passengers in 2016 and 2017.


import pandas as pd

# Load the CSV file into a DataFrame
airline_bumping = pd.read_csv("airline_bumping.csv")

# For each airline, calculate the sum of nb_bumped and total_passengers
airline_totals = airline_bumping.groupby('airline')[['nb_bumped', 'total_passengers']].sum()

# Create a new column called bumps_per_10k
airline_totals['bumps_per_10k'] = airline_totals['nb_bumped'] / airline_totals['total_passengers'] * 10000

# Print the result
print(airline_totals)

#4Print airline_totals to see the results of your manipulations.

# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)



