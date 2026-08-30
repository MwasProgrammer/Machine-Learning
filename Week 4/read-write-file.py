# Writing files in Python
with open('daily-log.txt', 'w') as file:
    file.write("Daily log entry for daily habits.\n")
    file.write("1. Exercise for 30 minutes.\n")
    file.write("2. Read a book for 1 hour.\n")
    file.write("Steps: 9200\n")
    file.write("Water: 8 glasses\n")
    file.write("Protocol: OMAD\n")
    file.write("Cold shower: Yes\n")

print("Reading the content of the file after writing:\n")

# Reading files in Python - reads the entire content of the file
with open('daily-log.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading files in Python - reads the file line by line
print("Reading the content of the file line by line:\n")
with open('daily-log.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        print("Line: ", line)

print(f"\nAppending new content to  a file.\n")
# Appending to files in Python
with open('daily-log.txt', 'a') as file:
    file.write("Newly updated habit - scuba diving. \n")

with open('daily-log.txt', 'r') as file:
    content = file.read()
    print(content)

# Processing file data
# Parse the lines into a dictionary
print("Processing file data and parsing it into a dictionay\n")

file_data = """
Steps: 9200
Water: 8
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
Pages read: 30
"""

log = {}
for line in file_data.strip().split('\n'):
    key, value = line.split(':')
    log[key.strip()] = value.strip()

print("\n Parsed log data:")
for key, value in log.items():
    print(f"{key}: {value}")