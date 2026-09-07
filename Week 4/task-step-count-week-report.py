# Create a Python dictionary called week_report that contains your name, 
# a list of 5 daily step counts, and the fasting protocols used each day. 
# Convert it to a JSON string and print it. Then load it back and 
# compute the average steps from the list inside the JSON.

import json

week_report = {
    "name": "Peter Mwangi",
    "daily_steps": [9000, 5500, 10500, 7950, 8800],
    "fasting_protocols": ["0MAD", "2MAD", "Autophagy Marathon", "0MAD", "2MAD"]
}

week_report_json = json.dumps(week_report)

print("JSON Week Report:", week_report_json)

loaded_week_report_python = json.loads(week_report_json)

average_steps = sum(loaded_week_report_python['daily_steps']) / len(loaded_week_report_python['daily_steps'])

print("Average Steps:", round(average_steps))