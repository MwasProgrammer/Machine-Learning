# Step count week program

steps_per_day = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
daily_target = 8000
minimum_steps = 5000
days_met_target = 0

for steps in steps_per_day:
    if steps <= minimum_steps:
        days_met_target += 1
        print(f"Skipped day {days_met_target} with {steps} steps.")
        continue