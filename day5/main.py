file = open("input.txt", "r")

def display_ship(ship):
    print("")
    display_rows = []
    for stack in ship:
        print(f"Stack: {stack}")

ship = []
for line in file:
    if "[" not in line:
        break
    formatted_line = line.replace("\n", "")
    crates = [formatted_line[i:i+4].strip() for i in range(0, len(formatted_line), 4)]
    ship.append(crates)

longest_row = len(max(ship, key=len)) # get longest list in ship

stacked_ship = []
for x in range(0, longest_row):
    new_stack = []
    for stack in ship:
        if stack[x] != "":
            new_stack.append(stack[x])
    new_stack = new_stack[::-1]
    stacked_ship.append(new_stack)

display_ship(stacked_ship)

# now we have array of stacks
# can append/pop to and from
for line in file:
    if "move" not in line:
        continue
    line = line.strip()
    instruction = line.split(" ")
    # stacked_ship[int(instruction[5])-1].extend([stacked_ship[int(instruction[3])-1].pop() for _ in range(0, int(instruction[1]))])

    temp = []
    for quantity in range(0, int(instruction[1])):
        popped_item = stacked_ship[int(instruction[3])-1].pop()
        temp.append(popped_item)
    temp = temp[::-1]
    stacked_ship[int(instruction[5])-1].extend(temp)
    display_ship(stacked_ship)

for stack in stacked_ship:
    print(stack.pop())
    