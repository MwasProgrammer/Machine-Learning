# A metalwork workshop tracking jobs by material type uses groupby 
# to answer "which material generates the most revenue?" in a single line. 

import pandas as pd

df = pd.DataFrame({
    "client":   ["Wanjiru", "Otieno", "Kamau", "Mwangi", "Njeri",  "Odhiambo", "Achieng", "Bett"],
    "item":     ["gate",    "grills", "frame", "gate",   "grills", "tank stand","frame",   "gate"],
    "material": ["mild steel","angle iron","hollow tube","mild steel","angle iron","mild steel","hollow tube","mild steel"],
    "price_kes":[28000, 14500, 9800, 32000, 12000, 18500, 11000, 29500],
    "status":   ["paid","paid","pending","paid","paid","pending","paid","paid"],
})

df["region"] = ["Nairobi", "Kiambu", "Machakos", "Kiambu", "Machakos", "Machakos", "Kiambu", "Machakos"]
print(df)
print()
print("Revenue by material type:")
by_material = df.groupby("material")["price_kes"].agg(["sum","mean","count"]).round(0)
by_material.columns = ["total_kes", "avg_kes", "jobs"]
print(by_material.sort_values("total_kes", ascending=False).to_string())

print("\nPaid vs pending jobs:")
print(df["status"].value_counts())

print("\nAverage job value by status:")
print(df.groupby("status")["price_kes"].mean().round(0))

print("\nRegions that earn most per job type:")
print(df.groupby("region")["material"].value_counts())

print()

# 1. Group by region and material, then sum up the price
region_material_revenue = df.groupby(["region", "material"])["price_kes"].sum().reset_index()

# 2. Sort by revenue so the highest earning combinations rise to the top
sorted_revenue = region_material_revenue.sort_values("price_kes", ascending=False)

print(sorted_revenue.to_string(index=False))