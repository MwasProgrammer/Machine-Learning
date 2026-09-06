import csv
import io

# Simulated CSV content
csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi
Grace Achieng,0745678901,copywriting,Kisumu
Brian Kamau,0756789012,upholstery,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)

# Skipping the header row
next(reader)

for row in reader:
    name, phone, skill, city = row
    print(f"{name} | {skill} | {city}")