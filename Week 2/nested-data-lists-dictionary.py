# Nested data - a list of dictionaries

week_logs = [
    {"day" : "Monday", "read_book" : True, "steps" : 1212},
    {"day" : "Tuesday", "read_book" : False, "steps" : 7829},
    {"day" : "Wednesday", "read_book" : True, "steps" : 12718},
    {"day" : "Thursday", "read_book" : True, "steps" : 9748},
    {"day" : "Friday", "read_book" : False, "steps" : 13231}
] 

print(week_logs)

# To print 
print(f"3rd day of the week: {week_logs[2]['day']}, it is {week_logs[2]['read_book']} that I read a book.")

# Looping through a list of dictionaries.
for log in week_logs:
    if log['steps'] >= 8000:
        print(f"{log['day']} Goal smashed. Steps covered - {log['steps']}")
    else:
        print(f"{log['day']} - Press on.")

print()

#Adding a new dictionary key-value to all the dictionaries in the list at once.
for log in week_logs:
    log['cold_showers'] = True
print(week_logs)

print()

# A dictionary with a list as a value
week_summary = {
    "week" : 1,
    "steps" : [912, 20139, 9312, 3942, 9892, 10102, 7382],
    "book_read_each_day" : False
}

print(f"Week: {week_summary['week']}")
print(f"Total days tracked: {len(week_summary['steps'])}")
print(f"Week's average steps: {sum(week_summary['steps'])//len(week_summary['steps'])}")


