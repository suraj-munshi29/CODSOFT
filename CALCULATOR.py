import numpy as np

print("Enter two numbers from the User :")
n1 = float(input("Enter the first number :"))
n2 = float(input("Enter the second number :"))

print("\n Choose your operation :- ")
print("1.Addition (+)")
print("2.Subtraction (-)")
print("3.Multiplication (*)")
print("4.Division (/)")
print("5.Modulous(%)")

choice = input("Enter your choices (1),(2),(3),(4),(5) :")
if choice == "1":
  result = n1 + n2
  print(f"\nResult = {n1}+{n2} ={result}")

elif choice == "2":
  result = n1 - n2
  print(f"\nResult = {n1}-{n2} ={result}")

elif choice == "3":
  result = n1 * n2
  print(f"\nResult = {n1}*{n2} ={result}")

elif choice == "4":
  if n2 != 0:
    result = n1 / n2
    print(f"\nResult = {n1}/{n2} ={result}")
  else:
    print("\nError! The number cannot be divided by Zero")
elif choice == "5":
  result = n1 % n2
  print(f"\nResult = {n1}%{n2} ={result}")
else:
  print("\n Invalid Choice . Please select among 4 options (1,2,3,4,5)")
  
