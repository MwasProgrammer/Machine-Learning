# API (Application Programming Interface) is a 
# set of rules that lets one program request data or 
# actions from another program over a network. 

# API simulated response.

# Simulates what response.json() returns from a fitness API
data = {
    "user_id": 1,
    "name": "James Omondi",
    "date": "2024-11-18",
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5,
    "workout_completed": True
}

print("Name:", data["name"])
print("Steps:", data["steps"])
print("Protocol:", data["fasting_protocol"])
print("Cold shower:", data["cold_shower"])
print("Sleep:", data["sleep_hours"], "hours")

# Accessing Nested Data
nested_data = {
    "user": {
        "id": 1,
        "name": "Sandra Weru",
        "city": "Nairobi"
    },
    "metrics": {
        "steps": 10500,
        "sleep_hours": 8.0,
        "bench_press_kg": 80
    },
    "skills": ["welding", "tiling", "copywriting"]
}

print("\nNested Data Access:")
print(nested_data["user"]["name"])
print(nested_data["user"]["city"])
print(nested_data["metrics"]["steps"])
print(nested_data["metrics"]["bench_press_kg"], "kg bench press")
print("Skills:", nested_data["skills"])
print("First skill:", nested_data["skills"][0])

print("\nLooping through a list response")

# Looping through a list response
# Simulates: response.json() from /api/weekly-logs
weekly_logs = [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "OMAD"},
    {"day": "Friday",    "steps": 7600,  "protocol": "2MAD"},
]

for log in weekly_logs:
    status = "Goal met" if log["steps"] >= 10000 else "Short"
    print(f"{log['day']:12} {log['steps']:6} steps  {status}")

print("\nUsing .get() for Missing Keys")

# Using .get() for Missing Keys
records = [
    {"name": "Patrick Njiru", "steps": 9100, "water_glasses": 7},
    {"name": "Grace Achieng", "steps": 8400},           # no water logged
    {"name": "Brian Kamau",   "steps": 10200, "water_glasses": 9},
]

for record in records:
    water = record.get("water_glasses", "not logged") # Use .get() with a default to handle it safely.
    print(f"{record['name']}: steps={record['steps']}, water={water}")


print("\nFiltering API Results")
# Filtering API Results
# Filter using the list comprehension pattern
logs = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD"},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD"},
    {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD"},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD"},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD"},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD"},
]

# OMAD users who hit 10,000 steps
goal_hitters = [
    r for r in logs
    if r["protocol"] == "OMAD" and r["steps"] >= 10000
]

print("OMAD users who hit 10k steps:")
for r in goal_hitters:
    print(f"  {r['name']}: {r['steps']} steps")