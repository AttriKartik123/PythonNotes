#Fill in missing values and sum values with pivot tables
#The .pivot_table() method has several useful arguments, including fill_value and margins.

#fill_value replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course (Dealing with Missing Data in Python), but the simplest thing to do is to substitute a dummy value.
#margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: it gives the row and column totals of the pivot table contents.
#In this exercise, you'll practice using these arguments to up your pivot table skills, which will help you crunch numbers more efficiently!

#sales is available and pandas is imported as pd.

#Print the mean weekly_sales by department and type, filling in any missing values with 0.
#2
#Print the mean weekly_sales by department and type, filling in any missing values with 0 and summing all rows and columns.

# Part 1: Fill missing values with 0
print("# Print mean weekly_sales by department and type; fill missing values with 0")
mean_sales_by_dept_type = sales.pivot_table(
    values="weekly_sales",
    index="department",
    columns="type",
    fill_value=0
)
print(mean_sales_by_dept_type)
print("------------------------------------------")

# Part 2: Add margins
print("# Print mean weekly_sales by department and type; fill missing values with 0 and sum all rows and columns")
mean_sales_by_dept_type_margins = sales.pivot_table(
    values="weekly_sales",
    index="department",
    columns="type",
    fill_value=0,
    margins=True
)
print(mean_sales_by_dept_type_margins)




#Print the mean weekly_sales by department and type, filling in any missing values with 0 and summing all rows and columns.


import pandas as pd

# Load your sales data if not already loaded (assuming 'sales' DataFrame is available)
# sales = pd.read_csv('your_sales_data.csv')

# Use .pivot_table() to get the mean weekly_sales
mean_sales_by_dept_type = sales.pivot_table(
    values='weekly_sales', 
    index='department', 
    columns='type', 
    fill_value=0, 
    margins=True
)

# Print the resulting pivot table
print(mean_sales_by_dept_type)


