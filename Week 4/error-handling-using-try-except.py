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