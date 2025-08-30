#Finding missing values
#Missing values are everywhere, and you don't want them interfering with your work. Some functions ignore missing data by default, but that's not always the behavior you might want. Some functions can't handle missing values at all, so these values need to be taken care of before you can use them. If you don't know where your missing values are, or if they exist, you could make mistakes in your analysis. In this exercise, you'll determine if there are missing values in the dataset, and if so, how many.

#pandas has been imported as pd and avocados_2016, a subset of avocados that contains only sales from 2016, is available.

##Print a DataFrame that shows whether each value in avocados_2016 is missing or not.
#Print a summary that shows whether any value in each column is missing or not.
#reate a bar plot of the total number of missing values in each column.

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt
# Print a DataFrame that shows whether each value in avocados_2016 is missing or not.
print(avocados_2016.isna())

# Print a summary that shows whether any value in each column is missing or not.
print(avocados_2016.isna().any())

# Create a bar plot of the total number of missing values in each column.
avocados_2016.isna().sum().plot(kind='bar')

# Show the plot
plt.show()