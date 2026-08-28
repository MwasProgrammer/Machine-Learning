steps_count = [3738, 8382,10212, 7539, 9483]

print('Steps walked from Monday to Friday', steps_count)

steps_count.append(10500)
print('List with Saturday added record', steps_count)

steps_count.remove(8382)
print('Removed item from list: ', steps_count)

steps_count.sort(reverse=True)
print('Sort list in Descending Order', steps_count)

goals_reached_day = 0
for steps in steps_count:
    if steps > 9000:
        goals_reached_day += 1
        # print(steps)
        print(f"Days that you reached targeted goals: {goals_reached_day}")
    else:
        print('9000 target goal not reached - ', steps)
