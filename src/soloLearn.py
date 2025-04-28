#01 --------------BMI CALCULATOR--------------
def bmi(weight, height):
    index = weight / (height * height)
    return index
    
patient_5 = bmi(61, 1.82)
print("underweight:", patient_5 < 18.5)

patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)


#02 --------------Perimeter CALCULATOR--------------
def rect(length, width):
    area = length*width
    perimeter = 2 * length + 2 * width
    return area, perimeter
    
x,y = rect(50,100)
print(x,y)


#03 -------------- V2 Perimeter CALCULATOR--------------
def rect(length, width):
    area = length*width
    perimeter = 2 * length + 2 * width
    return area, perimeter
    
x,y = rect(24,148)
print("Area:",x)
print("Perimeter",y)
print(x,y)

