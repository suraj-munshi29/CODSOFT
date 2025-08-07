import random
import string

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters  = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password
try:
  length = int(input("Enter the password length : "))
  if length <= 0:
    print("Please enter a positive number")
  else:
    password = generate_password(length)
    print(generate_password(length))
except ValueError:
  print("You are requested to enter a valid number.")
