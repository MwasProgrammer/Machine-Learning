import pandas as pd

df = pd.DataFrame({
    "city":     ["Nairobi", "Nairobi", "Mombasa", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Kisumu"],
    "protocol": ["OMAD",    "2MAD",    "OMAD",    "2MAD",    "OMAD",    "OMAD",   "2MAD",    "2MAD"],
    "steps":    [9200, 10500, 8100, 11000, 9400, 10200, 7400, 8800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 7.5, 8.0, 9.0, 7.5],
})

df["bench_press_kg"] = [80, 82, 78, 85, 80, 83, 84, 81]

print(df)
print()
# Average steps grouped by both city and protocol
breakdown = df.groupby(["city", "protocol", "bench_press_kg"])["steps"].mean().round(0)
print("Average steps by city and protocol:")
print(breakdown)

print()
print("Average bench press per protocol.")
bench_press = df.groupby(["protocol"])["bench_press_kg"].mean()
print(bench_press)