# Applied Example: Chicken Farm Egg Collection Log
# A chicken farmer records daily egg collection and feed cost per pen.

chicken_farm_data = """
Pen 1: Eggs: 12, Feed Cost: ksh30.00
Pen 2: Eggs: 15, Feed Cost: ksh40.00
Pen 3: Eggs: 10, Feed Cost: ksh20.50
"""
for line in chicken_farm_data.strip().split('\n'):
    line = line.strip()
    if ":" in line:
        pen, data_str = line.split(":", 1)
        eggs_str, feed_cost_str = data_str.split(",", 1)
        eggs = int(eggs_str.split(":")[1].strip())
        feed_cost = float(feed_cost_str.split(":")[1].strip()[3:])  # Remove 'ksh' and convert to float
        print(f"{pen}: {eggs} eggs collected, Feed Cost: ksh{feed_cost:.2f}")
