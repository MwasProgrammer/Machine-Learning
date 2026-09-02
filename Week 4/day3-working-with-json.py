import json

daily_log = {
    "steps" : 9250,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

# Convert the dictionary to a JSON string
daily_log_json = json.dumps(daily_log, indent=4)

print("Type:", type(daily_log_json))
print("JSON:", daily_log_json)

print()

print('JSON Text to Python text\n')
# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}'
api_data = json.loads(api_response)

print("\nType:", type(api_data))
print("Python Dictionary:", api_data)
print("Steps:", api_data["steps"])
print("Cold shower:", api_data["cold_shower"])
print("Protocol:", api_data["protocol"])

print()

print('JSON Text to Python text with nested data\n')
# Simulated API response with nested data
api_json = '''
{
  "client": "James Omondi",
  "week": 1,
  "daily_logs": [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 7600,  "protocol": "OMAD"},
    {"day": "Saturday",    "steps": 9740,  "protocol": "Masculinity Saturday"}
    
  ]
}
'''

data = json.loads(api_json)

print("Client:", data["client"])
print("Week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "low"
    print(f"  {log['day']}: {log['steps']} steps ({status})")

print(f"\nMonday records: Week:{data['week']} | {data['daily_logs'][0]}")