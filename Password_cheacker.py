# Password Strength Checker

import re

pwd = input("Enter password: ")

score = 0

if len(pwd) >= 8:
    score += 1
if re.search("[a-z]", pwd):
    score += 1
if re.search("[A-Z]", pwd):
    score += 1
if re.search("[0-9]", pwd):
    score += 1
if re.search("[@#$%^&*]", pwd):
    score += 1

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")
