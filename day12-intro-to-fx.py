# A function called day_report(steps, water, protocol) that prints a formatted report of a day's discipline data.

print(f"Day's habit track report.")
def day_report(day, steps, water, protocol):
    print(f"Day log: {day} report")
    print(f"Steps walked: {steps}.")
    print(f"Glasses of water drank: {water}.")
    print(f"Fasting protocol: {protocol}")


#Step goals tracker
def hit_goals(steps):
    for step in steps:
        if step >= 8000:
            return print('True')
        else:
            return print('False')


day_log = [
    {"day" : "Monday", "steps" : 3500, "water" : 8, "protocol" : "0MAD"},
    {"day" : "Tuesday", "steps" : 9500, "water" : 12, "protocol" : "Fasting"},
    {"day" : "Wednesday", "steps" : 7987, "water" : 4, "protocol" : "2MAD"}
]

day_report(steps, water, protocol)
hit_goals(steps)