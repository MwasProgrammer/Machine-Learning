step_profile = [
    {"name" : "Peter", "steps" : [7368, 9873, 10912, 6352, 8192, 5738, 7322]},
    {"name" : "Rael", "steps" : [9368, 7873, 10012, 6252, 7192, 5748, 9322]},
    {"name" : "Hanif", "steps" : [5368, 8973, 9412, 10352, 5192, 9738, 7622]},
    {"name" : "Jay", "steps" : [7648, 9863, 10972, 6351, 8592, 5838, 9322]},
]

steps_above_10000 = [profile for profile in step_profile if (step > 10000 for step in profile["steps"])]
print(f"Profiles with steps above 10000: {steps_above_10000}")