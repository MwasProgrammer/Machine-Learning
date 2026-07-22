steps_count = [3738, 8382,10212, 7539, 9483]

print('Steps walked from Monday to Friday', steps_count)

steps_count.append(10500)
print('List with Saturday added record', steps_count)

steps_count.remove(8382)
print('Removed item from list: ', steps_count)

steps_count.sort(reverse=True)
print('Sort list in Descending Order', steps_count)

for steps in steps_count:
    if steps > 9000:
        print(steps)
    else:
        print('9000 target goal not reached - ', steps)
