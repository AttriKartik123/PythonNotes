#Subsetting columns
#When working with data, you may not need all of the variables in your dataset. Square brackets ([]) can be used to select only the columns that matter to you in an order that makes sense to you. To select only "col_a" of the DataFrame df, use

#df["col_a"]
#To select "col_a" and "col_b" of df, use

#df[["col_a", "col_b"]]
#homelessness is available and pandas is loaded as pd.


#1
#Create a Series called individuals that contains only the individuals column of homelessness.

#Take Hint (-10 XP)
#2
#Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
#3
#Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order.


# Select the individuals column
individuals = homelessness["individuals"]

print(individuals.head())



# Select the state and family_members columns
state_fam = homelessness[["state" , "family_members"]]

print(state_fam.head())



# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals" , "state"]]

print(ind_state.head())



