import pandas as pd

patients = [
    {"name": "Alice",  "bp": 155, "glucose": 130, "creatinine": 0.9},
    {"name": "Brian",  "bp": 120, "glucose": 118, "creatinine": 1.5},
    {"name": "Carol",  "bp": 148, "glucose": 142, "creatinine": 1.0},
    {"name": "David",  "bp": 130, "glucose": 110, "creatinine": 0.8},
    {"name": "Eve",    "bp": 160, "glucose": 98,  "creatinine": 1.1},
    {"name": "Frank",  "bp": 125, "glucose": 115, "creatinine": 0.7},
]
df = pd.DataFrame(patients)

high_bp_patients = df[df["bp"] > 140]
print(f"Hypertension risk: {len(high_bp_patients)}")

diabetes_risk = df[df["glucose"] > 126]
print(f"Diabetes risk: {len(diabetes_risk)}")

kidney_disease_risk = df[df["creatinine"] > 1.2]
print(f"Kidney risk: {len(kidney_disease_risk)}")