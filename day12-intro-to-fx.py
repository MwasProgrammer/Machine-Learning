# A function called day_report(steps, water, protocol) that prints a formatted report of a day's discipline data.

def day_report(day, steps, water, protocol):
    print(f"\nDay log: {day} report")
    print(f"Steps walked: {steps}.")
    print(f"Glasses of water drank: {water}.")
    print(f"Fasting protocol: {protocol}")


#Step goals tracker
def hit_goals(steps):
    if steps >= 8000:
        return True
    else:
        return False

day_log = [
    {"day" : "Monday", "steps" : 3500, "water" : 8, "protocol" : "0MAD"},
    {"day" : "Tuesday", "steps" : 9500, "water" : 12, "protocol" : "Fasting"},
    {"day" : "Wednesday", "steps" : 7987, "water" : 4, "protocol" : "2MAD"}
]

print(f"Day's habit track report.")

for entry in day_log:
    day = entry["day"]
    steps = entry["steps"]
    water = entry["water"]
    protocol = entry["protocol"]    

    day_report(day, steps, water, protocol)

    goal_reached = hit_goals(steps)
    print(f"Steps target for {day} reached? {goal_reached}!\n")