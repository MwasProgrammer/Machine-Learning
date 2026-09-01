# Write a function called safe_log_entry(data) that 
# takes a dictionary and tries to extract steps, water, and protocol. 
# If steps is not a valid integer, print an error and return None. 
# If water is missing, use a default of 0. If protocol is missing, use "Unknown". 
# Print a clean report for each valid entry.

def safe_log_entry(data):
    try:
        steps = int(data.get("steps", 0))

    except (ValueError, TypeError):
        print(f"Error: Invalid steps value '{data.get('steps')}' for entry {data}.")
        return None

    water = data.get("water", 0)
    protocol = data.get("protocol", "unknown")

    print(f"Steps: {steps}, Water: {water} glasses, Protocol: {protocol}")

    return steps

entries = [
    {"steps": "10", "water": 5, "protocol": "Standard"},
    {"steps": "invalid", "water": 10, "protocol": "Advanced"},
    {"water": 15, "protocol": "Beginner"},
    {"steps": "100", "water": "5"}
]

results = [safe_log_entry(entry) for entry in entries]
valid_results = [result for result in results if result is not None]

print(f"\nValid steps entries: {len(valid_results)}")