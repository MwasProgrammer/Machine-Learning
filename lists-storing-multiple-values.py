# A list of my daily habits
daily_habits = [5, "Meditation", "Exercise", "Journaling"]

print(daily_habits)

print(f"I wake up at {daily_habits[0]} am. I  start my day with morning {daily_habits[1]}. Later, I {daily_habits[2]} and finish up with daily {daily_habits[3]}.")
print(daily_habits[-1])
append_habit = input("What habit would you like to add to your daily routine? ")
daily_habits.append(append_habit)
print(daily_habits[-1])
print(f"This list has {len(daily_habits)} items in it.")

# Add an empty space for better readability
print("\n")

# For loop to print each habit in the list
for habit in daily_habits:
    print(f"Habit: {habit}")

print(f"I want to edit the last habit in my list. I will replace {daily_habits[-1]} with a new habit.")
new_habit = input("What new habit would you like to add to your daily routine? ")
daily_habits[-1] = new_habit
print(f"My new habit is {daily_habits[-1]}.")

print("\n")

# Delete a habit from the list
print(f"Do you want to delete the last habit in your list? (yes/no) ")
delete_confirmation = input()
if delete_confirmation == 'yes':
    print(f"Deleting {daily_habits[-1]} from the list.")
    daily_habits.remove(daily_habits[-1])

else:
    print(f"Keeping {daily_habits[-1]} in the list.")

for habit in daily_habits:
        print(f"My final list of daily habits is: ")
        print(habit)

print("\n")

waking_time = [5, 5.30,6, 6.30, 7, 7.30, 8]

for time in waking_time:
    if time < 6:
        print(f"Early riser at {time} am.")
    elif time < 7:
        print(f"Moderate riser at {time} am.")
    else:
        print(f"Late riser at {time} am.")
