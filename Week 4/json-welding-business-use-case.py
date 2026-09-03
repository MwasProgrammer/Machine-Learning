import json

# A welding workshop stores job records as JSON
job_json = '''
{
  "workshop": "Kamau Metalworks",
  "location": "Gikomba, Nairobi",
  "jobs": [
    {"client": "Wanjiru",  "item": "gate",        "material": "mild steel", "quote_kes": 28000, "paid": true},
    {"client": "Otieno",   "item": "window grills","material": "angle iron", "quote_kes": 14500, "paid": false},
    {"client": "Mwangi",   "item": "door frame",   "material": "hollow tube","quote_kes": 9800,  "paid": true},
    {"client": "Adhiambo",   "item": "car welding",   "material": "metal fabric", "quote_kes": 10800,  "paid": false}
  ]
}
'''

data = json.loads(job_json)
print("Workshop:", data["workshop"])
print("Location:", data["location"])
print()

total = 0
paid = 0
for job in data["jobs"]:
    status = "PAID" if job["paid"] else "PENDING"
    print(f"  {job['client']}: {job['item']} - KES {job['quote_kes']:,} [{status}]")
    total += job["quote_kes"]
    if job["paid"]:
        paid += job["quote_kes"]

print(f"\nTotal quoted: KES {total:,}")
print(f"Collected:    KES {paid:,}")
print(f"Outstanding:  KES {total - paid:,}")
