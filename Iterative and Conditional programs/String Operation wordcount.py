#python program to enter a stringand count how many uppercase, lowercase, digits, words, present in it
str=input("Enter the sentence:")
u=0
l=0
d=0
space=0
dot=0
for i in str:
  if i.isupper():
    u+=1
  elif i.islower():
    l+=1
  elif i.isdigit():
    d+=1
  elif i.count(" "):
    space+=1
  elif i.count("."):
    dot+=1
  print("Uppercase:",u)
  print("Lowercase:",l)
  print("Digits:",d)
  w=space+dot
  print("Words:",w)
