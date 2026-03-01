## Making of simple calulator by Python 

num1 = float(input("Enter Your 1st Number: "))
num2 = float(input("Enter Your 2nd Number: "))

#choosing an operation

operation = input()

#performing calculation 

if operation == "+":
    print("Answer is : ", num1 + num2 )

elif operation == "-":
    print("Answer is : ", num1 - num2)

elif operation == "*":
    print("Answer is : ", num1 * num2)

elif operation == "/":
    print("Answer is : ", num1 / num2 )

else:
    print("Invalid Operation")