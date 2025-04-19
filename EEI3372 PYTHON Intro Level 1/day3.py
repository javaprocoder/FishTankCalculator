myList = [1,2,3,4,5,6,7]
print(myList)

myList.insert(1,"Hello")
print(myList)

myList.pop(1)
print(myList)

str = """Triple
        quites
        docstring"""
print(str)

#str1 = "Python"
#del str1
#print(str1)

def name():
    print("Hello there!")
    print("What is your Name?")
    
#Person 1
name()

#Person 1
name()

#Person 1
name()

#DEFINITION
def add(num1, num2):
    total = num1 + num2
    return total
    
#CALLING
print( add (24,45))
print( add (1,1))