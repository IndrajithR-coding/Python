#To take in 2 strings & display the larger string with/without using built-in function
x=input("Enter the first string:")
y=input("Enter the first string:")
z=int(input("0-Without f(x), 1-with f(x):"))
def w0f(x,y):
  countx=0
  county=0
  for i in x:
    countx+=1
  for i in y:
    county+=1
  if countx>county:
    print("Bigger string:",x)
  elif countx<county:
    print("Bigger string:",y)
  else:
    print("Both are equal strings!")

def w1f(x,y):
  c=max(x,y)
  print("Larger String:",c)

if z==0:
  w0f(x,y)
else:
  w1f(x,y)
print("Thank you!")
  
