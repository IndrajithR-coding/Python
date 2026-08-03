a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
n=input("Give a for first code, b for second code:")
if n==a:
  if a>b:
    if a>c:
      print(a," is the greatest number.")
    else:
      print(c," c is the greatest number.")
  else:
    if b>c:
      print(b," is the greatest number.")
    else:
      print(c," is the greatest number.")
elif n==b:
  if a>b:
    if a>c:
      print(a," is the greatest number.")
    else:
      print(c," is the greatest number.")
  elif b>c:
    print(b," is the greatest number.")
  else:
    print(c," is the greatest number.")
