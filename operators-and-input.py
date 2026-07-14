# Arithmetic Operators
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

#Taking user input
name = input("\nWhat is your name? ")
print(f"Hello, {name}! Welcome to the program.")

# Converting user input to integer
birth_year = input("Enter your birth year: ")
current_year = input("Enter the current year: ")
print(f"Sample test: ({birth_year}) + ({current_year})") #Interesting output
sample_sum = birth_year + current_year
print(f"Sample sum - treats integer as strings: {sample_sum}") 
print(f"You are {int(current_year) - int(birth_year)} years old.")

# Error handling for invalid input
user_input_age = input("\nWhat is your age? ")

try:
    age = int(user_input_age)
    print(f"You are {age} years old.")

except ValueError:
    print("Invalid input. Please enter a valid integer for age.")