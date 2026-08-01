#Python program to find Sale price of an item with given price and discount perent
a=eval(input("Enter the given price:"))
b=eval(input("Enter the discount:"))
c=a*(b/100)
d=a-c
print("Sale price=",d)
