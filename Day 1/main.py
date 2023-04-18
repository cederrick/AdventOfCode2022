with open('./Day 1/input.txt') as my_file:
    data = my_file.readlines()


counter = 0
new_data = []
for item in data:
    new_item = item.strip('\n')
    if new_item:
        new_item = int(new_item)
    new_data.append(new_item)


total = 0
totals = []
for item in new_data:
    if item:
        total += item
    else:
        totals.append(total)
        total = 0

print('part 1: ', max(totals))

totals.sort(reverse=True)

final = totals[0] + totals[1] + totals[2]

print(final)
