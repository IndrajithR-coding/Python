#Python program to check if a number is palindrome
num=eval(input("Enter the number:"))
temp=num
s=0
while (num>0):
  r=num%10
  s=s*10+r
  num=int(num/10)
if (s==temp):
  print("The number is a palindrome.")
else:
  print("The number is not a palindrome.")
