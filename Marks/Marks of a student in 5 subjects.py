#Marks of a student in 5 subjects
a=input("Student name:")
q=float(input("Enter the mark in Chemistry:"))
w=float(input("Enter the mark in Physics:"))
e=float(input("Enter the mark in CS:"))
r=float(input("Enter the mark in English:"))
t=float(input("Enter the mark in Mathematics:"))
total=q+w+e+r+t
perc=((total/500)*100)
print("Total:",total,"\t","Percentage:",perc)
