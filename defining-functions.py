# Defining a function block
def show_daily_goal():
    print("Target step goals: 8,000 steps.")
    print("Target water intake: 8 glasses.")
    print("Cold Shower: Yes")

show_daily_goal()

def hours_slept(hours):
    if hours >= 8:
        print('You have had good sleep', hours, 'hours.')

    elif hours >= 6:
        print('Consider adding more hours to your sleep', hours, 'hours.')

    else:
        print('Insufficient hours of sleep', hours, 'hours.')


hours_slept(1)
hours_slept(5)
hours_slept(6)
hours_slept(9)

print()

# Working with multiple parameters
print("Here are your KYC:")
def kyc_details(name, age, gender):
    print(f"Name: {name} | Age: {age} | Gender: {gender}")


kyc_details("Peter", 24, "Male")

print()

# Function with a return value
def calculate_weekly_steps_average(weekly_steps):
    total_steps = sum(weekly_steps)
    average_steps = total_steps/len(weekly_steps)

    return average_steps

def get_status(step_list):
    for step in step_list:
        if step >= 8000:
            return print(f"Target exceeded, steps taken {step}.")
        elif step >= 5000:
            return print(f"Target hit.")
        else:
            return print(f"Below target.")

step_list = [12322,1234,5432,12653,7643]
average_steps = calculate_weekly_steps_average(step_list)
print(f"Your weekly average steps are {average_steps} steps.")

print()

get_status(step_list)

print()

