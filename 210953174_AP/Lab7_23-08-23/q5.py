import re

string = input("Enter any Word to check for first and last same : ")

if re.findall('[A-Za-z]',string)[0] == re.findall('[A-Za-z]$',string)[0]:
    print("First and Last character are similar")
else:
    print("First and Last character are not similar")
