from random import randint
from math import floor

def generate_week():
    print(f"Hallas! Here is your weekly steps report:")
    weekly_steps = [randint(6000, 12000) for _ in range(7)]
    print(f"Weekly steps: {weekly_steps}\n")
    average_steps = floor(sum(weekly_steps)/len(weekly_steps))

    days_on_target = 0
    for steps in weekly_steps:
        if steps >= 8000:
            days_on_target += 1
            print(f"Steps {steps} - Target attained! | Average steps: {average_steps} | Days on target {days_on_target}")
            
        #print(f"Weekly steps: {steps} | Average steps: {average_steps} | Days on target {days_on_target}")
    
    
    
generate_week()
