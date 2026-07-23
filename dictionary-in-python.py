my_wellness_record = {
    "steps" : 18202,
    "water_glasses" : 9,
    # "hours_slept" : 4
}

print(f"Glasses of water drank: {my_wellness_record.get('water_glasses')}")

# ADD RECORD TO THE DICTIONARY
my_wellness_record["book_reading"] = True

print("Updated dictionary with new record", my_wellness_record)

# Deleting a key from a dictionary
my_wellness_record["to_be_deleted"] = "This is User Deletion Variable"
print('Wellness record: ', my_wellness_record)

del my_wellness_record["to_be_deleted"]
print('After Deletion', my_wellness_record)

# To check if key is in or not in the dictionary
if 'hours_slept' not in my_wellness_record:
    print('Sleep hours not yet recorded')

print('\n')

# Looping through a dictionary - through keys and values together.
for key, value in my_wellness_record.items():
    print(key, ':', value)

# Looping through a dictionary - through keys
for key in my_wellness_record.keys():
    print('The keys in my dictionary are', key)

# Looping through a dictionary - through values
for value in my_wellness_record.values():
    print('My values in my dictionary are ', value)