# Scope covered
# Functions, modules, and packages
# List comprehensions
# Default parameters

# Use a list comprehension to get all even numbers from 1 to 30
evens = [n for n in range(1, 31) if n % 2 == 0]
print(evens)

# Now get the squares of those even numbers
squares = [n**2 for n in evens]
print(squares)

print()

# Write a function that takes a list of scores
# and returns the average, highest, and lowest
def analyze_scores(scores):
    #sum = sum(scores)
    average = sum(scores)/ len(scores)
    highest = max(scores)
    lowest = min(scores)
    total = sum(scores)
    return total, average, highest, lowest

# Test the function
scores = [78, 92, 87, 67, 81]
total, average, highest, lowest = analyze_scores(scores)
print(f"Total: {total}, Average: {average}, Highest: {highest}, Lowest: {lowest}")

print()

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Amerix")
greet("Peter")