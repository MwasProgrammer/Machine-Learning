#with for loop - you know the number of iterations
for days in range(1,8):
    print(f"100000 steps for day {days}")


# while loop - you don't know the number of iterations. Code keeps running until a certain condition is met.
glasses_of_water = 0
while glasses_of_water < 8:
    glasses_of_water += 1
    print(f"Drink a glass of water. You have drank {glasses_of_water} glasses of water today.")


# break statement - used to exit a loop when a certain condition is met
steps_walked = 0
while steps_walked < 10000:
    steps_walked += 1000
    print(f"You have walked {steps_walked} steps today.")
    if steps_walked >= 10000:
        print("You have reached your step goal for the day!")
        break


# continue statement - used to skip the current iteration of a loop and move on to the next one
hours_slept = 0
while hours_slept < 8:
    hours_slept += 1
    if hours_slept == 6:
        print("You have slept for 6 hours. You need to sleep more.")
        continue
    print(f"You have slept for {hours_slept} hours today.")