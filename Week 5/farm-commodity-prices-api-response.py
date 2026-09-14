# Simulated response from a commodity prices API
commodity_response = {
    "status": "ok",
    "market": "Wakulima Market, Nairobi",
    "date": "2026-08-13",
    "prices": [
        {"commodity": "Maize",       "unit": "90kg bag", "price_kes": 3200, "change_pct": -2.1, "available": True},
        {"commodity": "Beans (Dry)", "unit": "90kg bag", "price_kes": 9800, "change_pct":  4.5, "available": True},
        {"commodity": "Milk (Raw)",  "unit": "litre",    "price_kes":   62, "change_pct":  1.2, "available": True},
        {"commodity": "Tea Leaf",    "unit": "kg",        "price_kes":   28, "change_pct": -0.8, "available": False},
        {"commodity": "Wheat Flour", "unit": "50kg bag", "price_kes": 2900, "change_pct":  0.0, "available": True},
    ]
}

market = commodity_response["market"]
date   = commodity_response["date"]
print(f"Market: {market}  |  Date: {date}")
print("-" * 55)
print(f"{'Commodity':<15} {'Unit':<12} {'Price (KES)':>12}  {'Change':>8}  Status")
print("-" * 55)

for item in commodity_response["prices"]:
    if not item["available"]:
        status = "OUT OF STOCK"
    elif item["change_pct"] > 0:
        status = "rising"
    elif item["change_pct"] < 0:
        status = "falling"
    else:
        status = "stable"
    change = f"{item['change_pct']:+.1f}%"
    print(f"{item['commodity']:<15} {item['unit']:<12} {item['price_kes']:>12,}  {change:>8}  {status}")

# available_items = []
# for available_item in commodity_response["prices"]:
#     if available_item["available"]:
#         available_items.append(available_item["commodity"])

# print("\nAvailable Commodities: ", available_items)

available_items = [item["commodity"] for item in commodity_response["prices"] if item["available"]]
print("\nAvailable Commodities: ", available_items)

commodity_with_highest_percentage_change = max(commodity_response["prices"], key=lambda x: abs(x["change_pct"]))
print(f"\nHighest percentage change: {commodity_with_highest_percentage_change['commodity']} ({commodity_with_highest_percentage_change['change_pct']:+.1f}%)")