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
# grocery_list = ["Flour", "Rice", "Sugar", "Dhal"]
# total_cost = 0

# for item in grocery_list:
#     if (item == "Sugar"):
#         continue
#     print("Buying", item)

#     item_price = int( input("Enter Current Item Price :"))
#     total_cost += item_price
#     print("Current Total Cost :", total_cost)

#     if total_cost > 500:
#         break

# print("Have a Happy Shopping!")
    

#Taking USER INPUT
# name = input("Enter Your Name -: ")
# age  = int (input("Enter Your Age  -: "))
# print("Your Name is", name)

# if age > 18:
#     print("You can Enroll to the Course")
# else: 
#     print("You are not Eligible to Enroll")

#Activity 01
moms_grocery_list = ["Sugar", "Bread", "Pasta", "Noodles"]
max_price_list = [350,490,820,680]
total_cost_moms = 0
budget = 2000

while total_cost_moms < budget:
    print("Lets Buy Something")

for item in moms_grocery_list:
    if (item == "Sugar"):
        continue
    print("Buying", item)

    item_price = int( input("Enter Current Item Price :"))
    total_cost_moms += item_price
    print("Current Total Cost :", total_cost_moms)

    if total_cost_moms > 600:
        break

print("You Have Done a Great Shopping My Son")
