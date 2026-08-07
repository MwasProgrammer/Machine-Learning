step_profile = [
    {"name" : "Peter", "steps" : [7368, 9873, 10912, 6352, 8192, 5738, 7322]},
    {"name" : "Rael", "steps" : [9368, 7873, 10012, 6252, 7192, 5748, 9322]},
    {"name" : "Hanif", "steps" : [5368, 8973, 9412, 10352, 5192, 9738, 7622]},
    {"name" : "Jay", "steps" : [7648, 9863, 10972, 6351, 8592, 5838, 9322]},
]

step_above_10000 = [day_steps for profile in step_profile for day_steps in profile["steps"] if day_steps > 10000]
print(f"\nList of profiles with steps above 10000: {step_above_10000}")

average_steps = [round(sum(profile["steps"]) / len(profile["steps"]), 2) for profile in step_profile]
average_steps_above_8500 = [profile["name"] for profile, avg in zip(step_profile, average_steps) if avg > 8500]
print(f"\nList of profiles with average steps above 8500: {average_steps_above_8500}")
    