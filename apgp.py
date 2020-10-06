# Python Program to find Sum of Arithmetic Progression Series

a = int(input("Please Enter First Number of an A.P Series: : "))
n = int(input("Please Enter the Total Numbers in this A.P Series: : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)
import math

x = int(input("Please Enter First Number of an G.P Series: : "))
y = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = (x * (1 - math.pow(r, y ))) / (1- r)
ty = x * (math.pow(r, y - 1))

print("\nThe Sum of Geometric Progression Series = " , total)
print("The tn Term of Geometric Progression Series = " , ty)
