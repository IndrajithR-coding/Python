#Python program to print the Fibonacci series.
n=eval(input("Enter the number of terms:"))
first=0
second=1
print(first)
print(second)
for x in range(2,n):
  third=first+second
  print(third)
  first=second
  second=third
