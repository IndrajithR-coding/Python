import math
a=eval(input("Enter the first side length:"))
b=eval(input("Enter the second side length:"))
c=eval(input("Enter the third side length:"))
s=(a+b+c)/2
print("s:",s)
h=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(h)
print("Area=",area)
