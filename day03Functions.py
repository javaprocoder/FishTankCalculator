# -------------------------DAY 03 PYTHON WORKSHOP-------------------------
# ------------------------CALCULATOR--------------------
# FUNCTIONS AS ARGUMENTS
def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def substract(num1, num2):  
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

while True:  
    num1 = int(input("Enter Number One: "))
    num2 = int(input("Enter Number Two: "))

    math_operation = input("Enter The Operator Symbol (+, -, *, /): ")

    if math_operation == "+":
        print("Result:", add(num1, num2))
    elif math_operation == "-":
        print("Result:", substract(num1, num2))
    elif math_operation == "*":
        print("Result:", multiply(num1, num2))
    elif math_operation == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid Operation!")

    repeat = input("Do you want to perform another calculation? (y/n): ").strip().lower()
    if repeat != "y":
        print("Goodbye!")
        break  
