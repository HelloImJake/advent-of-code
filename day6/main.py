file = open("input.txt", "r")

for line in file:
    datastream = line
characters = list(datastream)
for index, char in enumerate(characters):
    if index < 13:
        continue
    num_list = characters[index-13:index+1]
    new_set = set(num_list)
    if len(new_set) != 14:
        continue
    print(f"INDEX: {index+1}, CHARS: {num_list}")
    break
    