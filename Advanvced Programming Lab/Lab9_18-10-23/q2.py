class zeroDivision(Exception):
    pass

class lesserFirst(Exception):
    pass

class notReal(Exception):
    pass

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")

option = input("What would you like to do (+|-|*|/)? : ")

try:
    if not num1.isnumeric() or not num2.isnumeric():
        raise notReal
    
    num1 = int(num1)
    num2 = int(num2)

    if option == '+':
        print(num1+num2)
    elif option == '-':
        if num1 < num2:
            raise lesserFirst
        print(num1-num2)
    elif option == '*':
        print(num1*num2)
    elif option == '/':
        if num2 == 0:
            raise zeroDivision
        print(num1/num2)
        
except zeroDivision:
    print("Division by zero occurred")
except lesserFirst:
    print("num1 is lesser than num2")
except notReal:
    print("unreal numbers encountered")
