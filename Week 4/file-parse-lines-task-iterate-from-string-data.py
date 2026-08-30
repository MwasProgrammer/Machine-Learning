# Simulate writing a week of discipline logs as text lines, then read them back and
# count how many days recorded 8,000 or more steps. Use the split and strip
# techniques from this lesson to parse each line.

weekly_data = """
Monday: 7643
Tuesday: 8650
Wednesday: 8971
Thursday: 7647
Friday: 10375
Saturday: 5632
Sunday: 4900
"""

goal = 8000
days_on_goal = 0

#file = 'steps_weekly_log.txt'
    
for line in weekly_data.split('\n'):
    line = line.strip()
    if ":" in line:
        day, steps_str = line.split (":", 1)
        steps = int(steps_str.strip())    
        status = "Goal hit" if steps >= 8000 else "Below goal."
        print(f"{day}: {steps} steps - {status}")
        if steps >= goal: 
            days_on_goal += 1

print(f"\nDays on goal: {days_on_goal}/7")