name = input("What is your name? ")
print(f"Hello, {name}! I present to you my calculator.")

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

# Convert user input to float for calculations
float_first_number = float(first_number)
float_second_number = float(second_number)

# Perform arithmetic operations
print(f"\n Sum = {float_first_number + float_second_number}")
print(f" Difference = {float_first_number - float_second_number}")
print(f" Product = {float_first_number * float_second_number}")

# Division with error handling for division by zero
try:
    print(f"\n Quotient = {float_first_number / float_second_number}")
    print(f" Remainder = {float_first_number % float_second_number}") # Modulus operator to get the remainder
    print(f"No remainder = {float_first_number // float_second_number}") # Floor division operator to get the quotient without remainder

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
