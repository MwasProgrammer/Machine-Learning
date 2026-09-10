import csv
import io

# 1. Define the baseline social media data
# Adding 'platform_purpose' as an extra relevant metric to keep strategy focused
tracker_data = [
    {"platform": "WhatsApp", "current": 112, "target": 200, "purpose": "Broadcast/Direct Link"},
    {"platform": "LinkedIn", "current": 185, "target": 350, "purpose": "Professional/B2B"},
    {"platform": "Instagram", "current": 14, "target": 100, "purpose": "Visual/Brand"},
    {"platform": "TikTok", "current": 25, "target": 100, "purpose": "Short Video Discovery"},
    {"platform": "X (Twitter)", "current": 1, "target": 30, "purpose": "Networking/Text"},
    {"platform": "YouTube", "current": 13, "target": 50, "purpose": "Long & Short Video"},
    {"platform": "Substack", "current": 0, "target": 25, "purpose": "Owned Newsletter/Community"}
]

# 2. Setup an in-memory string file to hold our generated CSV content
csv_file = io.StringIO()

# 3. Define the column fields for DictWriter
fieldnames = ["Platform", "Current Followers", "3-Month Target", "Gap to Target", "Growth Needed (%)", "Platform Strategy"]

# 4. Initialize the DictWriter object
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

# 5. Process data and write rows dynamically
for item in tracker_data:
    current = item["current"]
    target = item["target"]
    
    # Calculate metrics
    gap = max(0, target - current)
    # Avoid dividing by zero if starting at 0 followers (like Substack)
    growth_needed_pct = round(((target - current) / current * 100), 1) if current > 0 else 100.0
    
    writer.writerow({
        "Platform": item["platform"],
        "Current Followers": current,
        "3-Month Target": target,
        "Gap to Target": gap,
        "Growth Needed (%)": f"{growth_needed_pct}%",
        "Platform Strategy": item["purpose"]
    })

# 6. Display the generated CSV format to the terminal
csv_file.seek(0)  # Reset file pointer to the beginning to read it
print("--- GENERATED CSV OUTPUT ---")
print(csv_file.read())

# 7. Print a clean, formatted dashboard view for quick scanning
print(f"\n{'Platform':<15} {'Current':>10} {'Target':>10} {'Gap':>8} {'Growth %':>10}")
print("-" * 58)
for item in tracker_data:
    gap = max(0, item["target"] - item["current"])
    growth = round(((item["target"] - item["current"]) / item["current"] * 100), 1) if item["current"] > 0 else 100.0
    print(f"{item['platform']:<15} {item['current']:>10} {item['target']:>10} {gap:>8} {str(growth)+'%':>10}")
