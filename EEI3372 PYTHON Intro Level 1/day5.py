# Error Handling using Try Catch 5/31/2025

try :
    print("Hello")
    print(x)
except :
    print("Something went wrong")
else :
    print("Nothing went wrong")

# With Finally
try :
    print(x)
except :
    print("Something went wrong")
finally :
    print("The 'try except' is finished.")

# Try Catch In Calculations
def add(n1, n2):
    return n1 + n2

def divide(n1, n2):
    return n1 / n2

num1 = int(input("Enter Number One: "))
num2 = int(input("Enter Number Two: "))  

print("Addition of two numbers:", add(num1, num2))

try:
    print("Division of two numbers:", divide(num1, num2))  
except ZeroDivisionError:
    print("You can't divide a number by zero")
finally:
    print("Thank You")

