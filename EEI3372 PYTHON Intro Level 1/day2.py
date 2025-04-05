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