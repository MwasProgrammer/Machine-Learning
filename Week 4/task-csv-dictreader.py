# You have a simulated CSV of a week's step data. 
# Read it with DictReader, convert steps to integers, 
# filter out any days with steps below 7000 as invalid, 
# and print the average steps for the valid days only.

import csv
import io

csv_data = """day,steps,protocol
Monday,9200,OMAD
Tuesday,7500,2MAD
Wednesday,10500,OMAD
Thursday,4200,OMAD
Friday,8800,Autophagy Marathon
Saturday,11000,2MAD
Sunday,9600,OMAD"""

output = io.StringIO(csv_data)
reader = csv.DictReader(output)

valid_steps = []

for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps) 
        print(f"{row['day']}: {steps} steps | {row['protocol']} | Valid")

    else:
        print(f"{row['day']}: {steps} steps | {row['protocol']} | Invalid")

average_steps = sum(valid_steps) / len(valid_steps) if valid_steps else 0
print(f"\nAverage steps for valid days: {round(average_steps)}")