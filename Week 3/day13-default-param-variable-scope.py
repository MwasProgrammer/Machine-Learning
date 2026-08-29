def weekly_report(name, steps_list, goal=8000):
    days_on_target = 0
    for steps in steps_list:
        if steps >= goal:
            days_on_target += 1

    average_steps = sum(steps_list)/len(steps_list)
    print(f"Name: {name} | Total Days: {len(steps_list)} | Days on goal: {days_on_target} | Average Steps: {average_steps}")
    print()


weekly_report(name="Peter", steps_list=[2783,63723,9302,10293,8973])
weekly_report(name="Mary", steps_list=[12783,63723,9302,10293,8973], goal = 10000)
