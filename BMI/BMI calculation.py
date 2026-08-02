#Python program to calculate BMI of a person
kg=eval(input("Enter the weight:"))
m=eval(input("Enter the height(in m):"))
bmi=kg/(m***2)
print("BMI=",bmi)
if (bmi<18.5):
  print("Underweight!!")
elif bmi>=18.5 and bmi<=24.9:
  print("Normal! Good job!!")
elif bmi>=25 and bmi<=29.9:
  print("Overweight")
elif bmi>=30:
  print(!!Obese!!")
