# Default parameters
def check_steps(steps, goal = 8000):
    if steps >= goal:
        print(f"You walked {steps} steps today. Your {goal} target steps has been attained!")
    else:
        print(f"Steps {steps} - Your {goal} steps is yet to be attained.")


check_steps(6793)
check_steps(10901)

print()

#To override default parameter
check_steps(9837, goal=10000)

# Keyword arguments implementation
def classical_music_player(name, instrument, music_genre = "classical", music_part = 4):
    print(f"{name} | Instrument: {instrument} | Genre: {music_genre} | Music part: {music_part}")

# Positional arguments - following the order of the listed arguments
classical_music_player("Peter", "Trombone")

# Keyword arguments
classical_music_player(name = "Kylian Dictator", music_genre = "Jazz canaoe", instrument="Organ")

# BMI Calculator
print(f"\n BMI Calculator")
def calculate_bmi(weight_kg, height_metre):
    bmi = weight_kg / (height_metre**2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = 61
height = 1.82
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Weight: {weight} | Height: {height} | BMI: {bmi} | Category: {category}")