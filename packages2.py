# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))





#Suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:

#my_inv([[1,2], [3,4]])
#Which import statement will you need in order to run the above code without an error?

#Possible answers


#1 import scipy

#2 import scipy.linalg

#3 from scipy.linalg import my_inv

#4 from scipy.linalg import inv as my_inv

# ANS--------------- OPTION 4 IS CORRECT