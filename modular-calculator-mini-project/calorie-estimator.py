
def estimate_calories(steps, calories_per_step = 0.04):
    total_calories = steps * calories_per_step
    return total_calories

estimated_calories = estimate_calories(10000)
print(f"Estimated calories burned for 10,000 steps: {estimated_calories} calories.")

print()

print("=====Weekly Calorie Summary Report=====")
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_steps = [8492, 3923, 10932, 12133, 7859, 9732, 5738]

for day, steps in zip(days, daily_steps): # Iterate through each day and corresponding step count
    calories_burned = estimate_calories(steps)
    print(f"{day}: {steps} steps, Estimated calories burned: {calories_burned:.2f} calories.")
