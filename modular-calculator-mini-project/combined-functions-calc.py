import math
from datetime import date

client_name = "Peter"
weight_kg = 65
height_meters = 1.83
weekly_steps = [7409, 9843, 3829, 9053, 10431, 9582, 7308]
protocols = ['0MAD', '0MAD', '2MAD', 'NEAT', 'Autophagy Marathon', '0MAD', '0MAD']
step_goal = 8000

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 1)

def bmi_category(bmi):
    if bmi < 18.25:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal weight'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obesse'

def weekly_steps_summary(steps):
    days_on_target = len([step for step in steps if step >= step_goal])
    total_steps = sum(steps)
    average_steps = total_steps / len(steps)
    return total_steps, average_steps, days_on_target

def estimate_calories(steps, calories_per_step=0.04):
    total_calories = steps * calories_per_step
    return math.floor(total_calories)

def protocol_summary(protocol_list):
    unique = list(set(protocol_list))
    summary = {}

    for protocol in unique:
        summary[protocol] = protocol_list.count(protocol)
    return summary

print(f"Client Name: {client_name.upper()}")
print(f"Date: {date.today()}\n")
print(f"Weight: {weight_kg} kg | Height: {height_meters} m")
print(f"BMI: {calculate_bmi(weight_kg, height_meters)} ({bmi_category(calculate_bmi(weight_kg, height_meters))})\n")

total_steps, average_steps, days_on_target = weekly_steps_summary(weekly_steps)
print(f"Weekly Steps Summary:")
print(f"  Total Steps: {total_steps}")
print(f"  Average Steps: {average_steps:.0f}")
print(f"  Days on Target: {days_on_target}\n")

print(f"Estimated Calories Burned: {estimate_calories(total_steps)}\n")

print(f"Protocol Summary:")
for protocol, count in protocol_summary(protocols).items():
    print(f"  {protocol}: {count}")