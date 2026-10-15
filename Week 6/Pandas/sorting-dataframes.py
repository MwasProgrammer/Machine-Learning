import pandas as pd

df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5],
})

# Sort by steps, highest first
ranked = df.sort_values("steps", ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1  # 1-based ranking

# sort by sleep_hours in descending order.
ranked_sleep_hours = df.sort_values("sleep_hr", ascending=False).reset_index(drop=True)
most_sleep = df[df["sleep_hr"] == df["sleep_hr"].max()]
print(f"\nPerson with the most hours of sleep:")
print(most_sleep[["name", "sleep_hr"]])
print()

df["wake_up_score"] = (df["sleep_hr"]*df["steps"])/1000

wake_up_rank = df.sort_values("wake_up_score", ascending=True).reset_index(drop=True)

print("Wake Up Score Leaderboard (Ascending):")
print(wake_up_rank[["name", "wake_up_score"]].to_string())

print()

print("Step leaderboard:")
for i, row in ranked.iterrows():
    print(f"  #{i}  {row['name']:<20} {row['steps']:,} steps")