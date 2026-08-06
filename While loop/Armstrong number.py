#Python program to check if a number is armstrong number
ab=eval(input("Enter the number:"))
temp=ab
s=0
while ab>0:
  r=ab%10
  s+=r**3
  ab=int(ab/10)
if s==temp:
  print("Armstrong number.")
else:
  print("Not Armstrong number.")
