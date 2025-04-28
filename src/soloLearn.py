#01 --------------BMI CALCULATOR--------------
def bmi(weight, height):
    index = weight / (height * height)
    return index
    
patient_5 = bmi(61, 1.82)
print("underweight:", patient_5 < 18.5)

patient_7 = bmi(75, 1.74)
print("underweight:", patient_7 < 18.5)