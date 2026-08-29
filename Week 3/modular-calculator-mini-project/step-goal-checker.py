def daily_step_count(step_list, goal=8000):
    week_sum_step = sum(step_list)
    week_avg_step = (round(week_sum_step/len(step_list)))

    print(f"Total steps walked this week: {week_sum_step} steps.")
    print(f"Average steps walked this week: {week_avg_step} steps.")

    if week_sum_step >= goal:
        print(f"Weekly step target reached. {week_sum_step} steps.")
    else:
        print("Weekly step target failure.")

print("=====Weekly Step Summary Report=====")
daily_step_count([6723, 29382, 2324, 1341, 3654, 9859, 9231])