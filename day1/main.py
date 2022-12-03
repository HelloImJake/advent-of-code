file = open("input.txt", "r")

calorie_totals = []
running_total = 0
for line in file:
    if line == "\n":
        calorie_totals.append(running_total)
        running_total = 0
        continue
    running_total += int(line)
calorie_totals.append(running_total)

print(calorie_totals)
calorie_totals.sort(reverse=True)
print(calorie_totals)
print(sum(calorie_totals[:3]))
        