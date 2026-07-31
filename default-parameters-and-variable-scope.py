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