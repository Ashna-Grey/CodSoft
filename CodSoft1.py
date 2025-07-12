#task 2
def calculate():
    operation=input("Enter + - * or /: ")
    if operation in ("+", "-", "*", "/"):
        num1,num2=[float(input(f"Enter {'numerator' if i==0 and operation=='/' else 'denominator' if i==1 and operation=='/' else 'a number'}: ")) for i in range(2)]
        if operation=="+":
            print(f"{num1}+{num2} = {num1+num2}\n")
        elif operation == "-":
            print(f"{num1}-{num2} = {num1-num2}\n")
        elif operation == "*":
            print(f"{num1}*{num2}={num1*num2}\n")
        else:
            if num2==0:
                print("Error: Division by zero.\n")
            else:
                print(f"{num1}/{num2}={num1/num2}\n")
    else:
        print("Incorrect input.\n")
calculate()
while True:
    ch=input("Do you want to continue?\nEnter Y for yes and N for no.: ")
    if ch.lower() in ("y","n"):
        if ch.lower()=="y":
            calculate()
        else:
            print("Thank you.")
            break
    else:
        print("Incorrect input. Please enter Y or N.")

