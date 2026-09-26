import json

# Simulated API response from a welding supplier
response_text = '''
{
    "supplier": "Nairobi Steel Ltd",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800
    }
}'''

data = json.loads(response_text)

stock = {"mild_steel_sheet": 3, "angle_iron_in_metres": 6}

mild_steel_sheet_price = data["prices"]["mild_steel_sheet"]
angle_iron_price = data["prices"]["angle_iron"]

total_cost = (stock["mild_steel_sheet"] * mild_steel_sheet_price) + (stock["angle_iron_in_metres"] * angle_iron_price)

print(f"Mild steel sheets (3): KES {stock['mild_steel_sheet'] * mild_steel_sheet_price}")
print(f"Angle iron (6m): KES {stock['angle_iron_in_metres'] * angle_iron_price}")
print(f"Total cost: KES {total_cost}")