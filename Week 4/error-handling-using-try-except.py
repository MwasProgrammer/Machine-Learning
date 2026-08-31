# try and except
# Wrap code that might fail in a try block. 
# Put your response in the except block. 
# If the try block fails, Python jumps to except instead of crashing.

steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data:
    try:
        steps = int(item)
        if steps >= 8000:
            print(steps, "- Goal hit")
        else:
            print(steps, "- Below goal")
    except ValueError:
        print(f"'{item}' is not a valid number. Skipping.")

print()

print('Running multiple try-except blocks\n')

# A dairy farmer records daily milk output (litres) from 3 cows.
# Some days the entry is wrong or missing.

def calculate_daily_average(milk_records):
    try:
        total = sum(milk_records)
        avg = total / len(milk_records)
        return round(avg, 2)
    except ZeroDivisionError:
        print("Error: No records found. Cannot calculate average.")
        return 0
    except TypeError:
        print("Error: Records contain non-numeric values.")
        return 0

print("Average litres:", calculate_daily_average([18.5, 20.0, 17.8, 19.2]))
print("Average litres:", calculate_daily_average([]))
print("Average litres:", calculate_daily_average([18.5, "missing", 17.8]))

print()

# else and finally
# A tiling contractor calculates cost per tile for each job.
# If zero tiles are entered by mistake, the program should not crash.

def cost_per_tile(total_cost, num_tiles):
    try:
        result = total_cost / num_tiles
    except ZeroDivisionError:
        print("Cannot divide: zero tiles entered.")
    else:
        print(f"KES {total_cost} / {num_tiles} tiles = KES {result:.2f} per tile")
    finally:
        print("(Calculation attempted)")
    print()

cost_per_tile(45000, 300)
cost_per_tile(30000, 0)
cost_per_tile(62400, 480)

print()

# raising exceptions
def wanttam(tenure):
    if not isinstance(tenure, int):
        raise TypeError("Tenure must be an integer.")

try:
    wanttam("five")
except TypeError as e:
    print(f"Error: {e}")

print('\nRaising exceptions with custom messages\n')
def log_steps(steps):
    if not isinstance(steps, int):
        raise TypeError("Steps must be an integer.")
    if steps < 0:
        raise ValueError("Steps cannot be negative.")
    print(f"Steps logged: {steps}")

try:
    log_steps(9200)
    log_steps(-500)
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)

print('\nError handling with data processing\n')

daily_logs = [
    {"day": "Monday",    "steps": "9200"},
    {"day": "Tuesday",   "steps": "not recorded"},
    {"day": "Wednesday", "steps": "10500"},
    {"day": "Thursday",  "steps": None},
    {"day": "Friday",    "steps": "8800"},
]

valid_steps = []
for log in daily_logs:
    try:
        steps = int(log["steps"])
        valid_steps.append(steps)
        print(f"{log['day']}: {steps} steps")
    except (ValueError, TypeError):
        print(f"{log['day']}: invalid data - skipped")

if valid_steps:
    avg = sum(valid_steps) / len(valid_steps)
    print(f"\nAverage from valid days: {round(avg)} steps")