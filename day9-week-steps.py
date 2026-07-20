week_steps = [6738, 7982,10192, 8902, 122, 7987, 12322]
minimum_steps = 8000

for steps in week_steps:
    if steps >= 10000:
        print(f"Superb! You walked {steps} steps today.\n")

    else:
        print(f"You walked {steps} steps today. You need to walk more to reach your goal.\n")

print(f"Days you met your target: {len([steps for steps in week_steps if steps >= minimum_steps])}")
print(f"Days tracked: {len(week_steps)}")