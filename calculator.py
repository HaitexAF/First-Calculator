Operation = input("pick your operation ...")
num1 = input("choose first number ...")
num2 = input("choose second number ...")
number1 = int(num1)
number2 = int(num2)
if Operation == "addition":
    print(number1 + number2)
elif Operation == "subtraction":
    print(number1 - number2)
elif Operation == "multiplication":
    print(number1 * number2)
elif Operation == "division": 
    print(number1 / number2)
else:
    print("I can't help you")
