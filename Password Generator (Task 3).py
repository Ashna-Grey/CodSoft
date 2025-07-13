#task 3:Random Password generator
import random

upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low=upper.lower()
digits="1234567890"
symbol="*/\#@!$%^&*()_-+=:;',<>./?"

#taking length of password
num,password=int(input("Enter length of password: ")),""

#Running complexity
ch1,ch2,ch3,ch4=[input(f"Do you want to add {i}? Enter (Y/N): ") for i in ["Upper-case alphabets", "Lower-case alphabets","Digits","Symbols"]]
choices=[]
if (ch1.lower()=="y"):
    choices.append(upper)
if (ch2.lower()=="y"):
    choices.append(low)
if (ch3.lower()=="y"):
    choices.append(digits)
if (ch4.lower()=="y"):
    choices.append(symbol)
if choices==[]:
    print("Incorrect input.")
    exit()

#Generating password 
while (len(password)!=num):
    r=random.choice(choices)
    password+=random.choice(r)

#printing password
print("Generated password: ",password)
