#Replacing missing values
#Another way of handling missing values is to replace them all with the same value. For numerical variables, one option is to replace values with 0— you'll do this here. However, when you replace missing values, you make assumptions about what a missing value means. In this case, you will assume that a missing number sold means that no sales for that avocado type were made that week.

#In this exercise, you'll see how replacing missing values can affect the distribution of a variable using histograms. You can plot histograms for multiple variables at a time as follows:

#dogs[["height_cm", "weight_kg"]].hist()
#pandas has been imported as pd and matplotlib.pyplot has been imported as plt. The avocados_2016 dataset is available.

#1A list has been created, cols_with_missing, containing the names of columns with missing values: "small_sold", "large_sold", and "xl_sold".
#Create a histogram of those columns.
#Show the plot.

# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()



#2A list has been created, cols_with_missing, containing the names of columns with missing values: "small_sold", "large_sold", and "xl_sold".
#Create a histogram of those columns.
#Show the plot.

# From previous step, define the list of columns with missing values.
# Based on the bar plot from the previous exercise, these are the columns with missing values.
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms of the original columns with missing values
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()
plt.show()