#Price of conventional vs. organic avocados
#Creating multiple plots for different subsets of data allows you to compare groups. In this exercise, you'll create multiple histograms to compare the prices of conventional and organic avocados.

#matplotlib.pyplot has been imported as plt and pandas has been imported as pd.

#1
#Subset avocados for the "conventional" type and create a histogram of the avg_price column.
#Create a histogram of avg_price for "organic" type avocados.
#Add a legend to your plot, with the names "conventional" and "organic".
#Show your plot.

# Create a histogram of avg_price for conventional avocados
avocados[avocados["type"] == "conventional"]["avg_price"].hist()

# Create a histogram of avg_price for organic avocados
avocados[avocados["type"] == "organic"]["avg_price"].hist()

# Add a legend to the plot
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


#2
#Modify your code to adjust the transparency of both histograms to 0.5 to see how much overlap there is between the two distributions.

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()


#3
#Modify your code to use 20 bins in both histograms.
# Create a histogram of avg_price for conventional avocados with 20 bins and transparency
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)

# Create a histogram of avg_price for organic avocados with 20 bins and transparency
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)

# Add a legend to the plot
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()
