#Python program to count the number of vowels
x=input("Enter the string:")
vowel=0
L=['a','e','i','o','u','A','E','I','O','U']
for i in x:
  if i in L:
    vowel+=1
print("No. of vowels=",vowel)
