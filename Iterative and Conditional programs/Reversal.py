#Python program to reverse an entered number
num=eval(input("Enter the number:"))
s=0
while (num>0):
  r=num%10
  s=s*10+r
  num=int(num/10)
print("Reversed number:", s)
