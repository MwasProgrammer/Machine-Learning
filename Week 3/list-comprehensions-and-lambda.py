# Building a list from an existing list using loops
weekly_steps = [2133, 8753, 4356, 9753, 10812, 7493, 12123]

target_hit_day = []

for steps in weekly_steps:
    if steps >= 8000:
        target_hit_day.append(steps)

print(f"List of above 8000 steps: {target_hit_day}")

# Building a list from an existing list using list comprehensions
target_less_steps = [steps for steps in weekly_steps if steps < 8000]
print(f"List of below 8000 steps: {target_less_steps}")

# Transforming items in a list comprehension
# Converting steps to kilometers
km_walked = [round(steps * 1.3 / 1000, 2) for steps in weekly_steps]
print(f"\nSteps walked: {weekly_steps} | \nSteps in KM: {km_walked}")

# Converting steps to calories burned
calories_burned = [round(steps * 0.04, 2) for steps in weekly_steps]
print("Calories burned: ", calories_burned)

print(f"\n Filtering a list of dictionaries using list comprehensions.")

clients = [
    {"name" : "Peter", "goal" : "fat-loss", "sessions" : 4},
    {"name" : "John", "goal" : "muscle gain", "sessions" : 5},
    {"name" : "Jane", "goal" : "fat-loss", "sessions" : 3},
    {"name" : "Kate", "goal" : "endurance", "sessions" : 7},
    {"name" : "James", "goal" : "fat-loss", "sessions" : 2},
]

print("Filtering clients with fat-loss goal using list comprehensions.")
fat_loss_clients = [client["name"]for client in clients if client["goal"] == "fat-loss"]
print(f"\nClients with fat-loss goal: {fat_loss_clients}")