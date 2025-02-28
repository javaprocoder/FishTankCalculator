#-------------------------DAY 03 PYTHON WORKSHOP-------------------------
#------------------------CALCULATOR--------------------
#FUNCTIONS AS ARGUMENTS
def add(num1,num2):
    return num1+num2

def multiply(num1,num2):
    return(num1*num2)

def substract(num1,num2):
    return(num1-num2)

def divide(num1,num2):
    return(num1/num2)

# print(add(10,30))
# print(add(8,5))

# #print(add(2,5) - (substract(10-2)) * 2 /2)
# print(substract(add(2,5),multiply(10,2)/2))

num1 = int(input("Enter Number One:"))
num2 = int(input("Enter Number two:"))

math_operation = input("Enter The Operator Symbol:")

if math_operation == "+":
    print(add(num1,num2))
elif math_operation == "-":
    print(substract(num1,num2))
elif math_operation == "*":
    print(multiply(num1,num2))
elif math_operation == "/":
    print(divide(num1,num2))
else:
    print("Invalid Operation!")