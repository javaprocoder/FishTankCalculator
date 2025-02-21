#-------------------------DAY 02 PYTHON WORKSHOP-------------------------
 
#While LOOPS
count = 0
while count < 6:
    print("I Love Sri-Lanka")
    count +=1

#For LOOPS
for count in range(1,6):
    print(count)
    print("I Love Python")

#LISTS
grocery_list = ["Flour", "Rice", "Sugar", "Dhal"]

for item in grocery_list:
    print("Buying", item)

#Taking USER INPUT
name = input("Enter Your Name -: ")
age  = int (input("Enter Your Age  -: "))
print("Your Name is", name)

if age > 18:
    print("You can Enroll")
else: 
    print("You are not Eligible to Enroll")