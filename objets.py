#-------------------------DAY 02 PYTHON WORKSHOP PART 2-------------------------
#FUNCTIONS
#defning the functions
def morning_greetin_message(person_name):
    print("Hello", person_name, "!")
    print("Good Morning")
    print("How are you ?")
    print("\n")

#calling the functions
#Meeting the first person
morning_greetin_message("John")

#Meeting the second person
morning_greetin_message("Saad")

#Meeting the third person
morning_greetin_message("Sharaf")

#Nested Loops -> Loops inside another Loop
a = 1
while (a<5):
    print(a)

    b = 1
    while(b<5):
        print(b)
        b+=1

    a+=1
    