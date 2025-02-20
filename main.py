print("--------Fist Tank Amount Calculator--------")

def calculate_capacity(length, width, height):
    capacity_liters = (length * width * height) * 0.001
    return capacity_liters

length = float(input("Enter the length of the tank (cm): "))
width = float(input("Enter the width of the tank (cm): "))
height = float(input("Enter the height of the tank (cm): "))

capacity = calculate_capacity(length, width, height)

print(f"The capacity of the Fish Tank is {capacity} liters.")