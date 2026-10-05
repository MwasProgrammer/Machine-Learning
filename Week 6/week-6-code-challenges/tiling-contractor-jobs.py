# Code Challenge 1 — Tiling Contractor Jobs
# A tiling contractor tracks jobs in a list of dictionaries. 
# Loop through the jobs below to calculate and 
# print total boxes laid and total revenue. 
# import micropip
# await micropip.install("pandas")
import pandas as pd

jobs = [
    {"client": "Kamau", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "boxes_used": 60, "price_per_box": 2200},
]

df = pd.DataFrame(jobs)

Total = df["boxes_used"].sum()

print("Total:", Total)

df["revenue"] = df["boxes_used"] * df["price_per_box"]

total_revenue = df["revenue"].sum()
print("Revenue: KES", total_revenue)