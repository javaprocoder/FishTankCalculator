# SWITCH
lang = "Python";
match lang:
    case "Javascript":
        print("Web Developer!")
    case "Java":
        print("Mobile and Backend Developer!")
    case "Python":
        print("Data Scientist!")
    case _:
        print("Language Not matched!")

# Loop
count = 0;
while count < 5:
    print("Hello");
    count += 1;

# for x in range(10):
#     print(x)

# for x in range(1, 10):
#     print(x)

# for x in range(1, 10, 2):
#     print(x)  

for x in range(2, 20, 2):
    print(x)

Months = ["Jan", "Feb", "Mar", "Apr", "May", "June"];
for m in Months:
    print(m);

# # Using Break Statements.
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# Using Continue Statements.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

vehicles = ["car", "van", "bus", "jeep", "lorry", "truck", "bike", "scooter"]
for x in vehicles:
    if x == "lorry":
        continue
    print(x)

# USER INPUT
name = input("Enter name:")
print("Your Name is: "+name)

age = int(input("Enter Age:"))
print("Your Age is: "+str(age))
# print("Your Age is: ",age)

# Create EMPTY LIST
my_list = []
print(my_list)
my_list = [1,2,3,'example',2.21]
print(my_list)

# SLICE
a = ["a", "b", "c", "d", "e", "f", "g", "h"]
