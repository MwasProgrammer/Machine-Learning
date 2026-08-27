#Exercise
# Create a file called day4.py. Write a daily discipline grader. Store the following values:

# Steps: 7500
# Sleep hours: 6
# Water glasses: 5
# Cold shower: False
# Pages read: 15
# Write conditions that grade each one and print a final verdict. For steps: excellent i

target_steps = 7500
target_sleep_hours = 8
target_water_glasses = 8
boolean_cold_shower = False
target_pages_read = 20

actual_steps = int(input("How many steps did you take today? "))
shower_input = input("Did you take a cold shower today? (True/False) ")

actual_shower = shower_input.lower() == 'false'

if actual_steps >= target_steps and actual_shower == boolean_cold_shower:
    print("Excellent! You have met your daily discipline goals.")

    if actual_steps < target_steps or actual_shower != boolean_cold_shower:
        print(f"Keep pushing, your goals are within reach! You walked {actual_steps}")

else:
    print("You did not meet your daily discipline goals. Keep trying!")


actual_pages_read = int(input("How many pages did you read today? "))
if actual_pages_read >= target_pages_read:
    print("Great job on reading! You have met your reading goal.")  

elif actual_pages_read >= target_pages_read/2:
    print("Good effort! You are halfway to your reading goal.")

elif actual_pages_read <= 5:
    print("You read a few pages today. Keep it up!")

else:
    print("You did not read enough today. Try to read more tomorrow!")
