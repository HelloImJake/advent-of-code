file = open("input.txt", "r")

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

items = []
priority = 0
for char in alphabet:
    priority += 1
    items.append({"item_type": char, "priority": priority})

def convert_item_to_priority(item_to_check) -> int:
    for item in items:
        if item["item_type"] == item_to_check:
            return item["priority"]

def calculate_priorities_for_group(group):
    item_1 = set(group[0])
    item_2 = set(group[1])
    item_3 = set(group[2])
    print(f"{item_1}, {item_2}, {item_3}")
    group_1_2 = sorted(item_1.intersection(item_2))
    group_2_3 = sorted(set(group_1_2).intersection(item_3))
    priority = convert_item_to_priority(group_2_3[0])
    return priority

total_priority = 0
elf = 0
current_group = []
running_total = 0
for line in file:
    current_group.append(line.strip())
    elf += 1
    if elf == 3:
        elf = 0
        # print(current_group)
        found_group = calculate_priorities_for_group(current_group)
        print("\n NEW GROUP")
        current_group = []
        running_total += found_group
        continue

print(running_total)


