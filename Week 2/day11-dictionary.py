# Dictionary containing records of daily habits
my_log = {
    # "steps" : 19212,
    "water_glasses" : 8,
    "fasting_protocol" : "OMAD",
    "cold_shower" : True,
    "sleep_hours" : 7
}

print(f"Daily Habits Track Record")
for key, value in my_log.items():
    print(f" {key} : {value}")

my_log['steps'] = int(input("Enter steps walked today: "))

if my_log['steps'] >= 8000:
    print(f"You have hit the goal for your Daily Steps! Steps walked: {my_log['steps']}")

else:
    print(f"Press on to reach your Daily Steps Goal!")