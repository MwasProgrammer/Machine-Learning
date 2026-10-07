import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
goal  = 10000

# All at once, no loop needed
deficit = steps - goal
print("Steps vs 10k goal:", deficit)

# Percentage of goal achieved
pct = (steps / goal * 100).round(1)
print("Percent of goal:", pct)

# Boolean mask: which days hit the goal?
hit = steps >= goal
print("Hit goal:", hit)
print("Days hitting goal:", steps[hit])