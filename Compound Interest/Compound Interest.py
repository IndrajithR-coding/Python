#Python program to calculate Compound Interest
a=eval(input("Enter the principal:"))
b=eval(input("Enter the rate of principal:"))
c=eval(input("Enter the number of times of interest:"))
d=a*(1+(b/100))**c
print("Compound Interest=",d)
