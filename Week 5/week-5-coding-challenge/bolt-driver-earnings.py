import json

# Simulated API response from a bolt driver rides
response_text = '''
{
    "driver": "Kamau Njoroge",
    "date": "2026-08-13",
    "trips": [
        {"route": "Westlands to CBD",     "fare_kes": 560},
        {"route": "CBD to South B",       "fare_kes": 420},
        {"route": "South B to Karen",     "fare_kes": 980},
        {"route": "Karen to Westlands",   "fare_kes": 720},
        {"route": "Westlands to Airport", "fare_kes": 740}
    ]
}'''

data = json.loads(response_text)

for trip in data["trips"]:
    driver = data["driver"]
    total_trips = len(data["trips"])
    earnings = sum(trip["fare_kes"] for trip in data["trips"])
    highest_earning_trip = max(data['trips'], key=lambda x: x['fare_kes'])

print(f"Total trips: {total_trips}")
print(f"Total earnings: KES {earnings}")
print(f"Highest trip: {highest_earning_trip['route']} | KES {highest_earning_trip['fare_kes']}")
