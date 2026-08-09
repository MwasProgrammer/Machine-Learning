# BMI Calculator function
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2) 
    return round(bmi, 1) 

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

    # Test the BMI calculator function
weight = 70  # in kilograms
height = 1.80 # in meters
bmi = calculate_bmi(weight, height)

print(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi}, Category: {get_bmi_category(bmi)}")