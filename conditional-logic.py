#if statement
steps = 10000

if steps >= 10000:
    print(f"You have reached your {steps} step goal for the day!")

# If statement with else
steps_walked = int(input("How many steps have you walked today? "))
if steps_walked >= 10000:
    print(f"You have reached your {steps} step goal for the day!")
else:
    print(f"You require {steps - steps_walked} more steps to reach your goal.")


#elif statement
temperature = int(input("What is the current temperature in Celsius? "))

if temperature > 30:
    print("It's a hot day.")
elif temperature >= 20:
    print("It's a pleasant day.")
else:
    print("It's a cold day.")


# And statement - both statements must be true
# Or statement - either statement can be true - atleast one of the statements must be true

