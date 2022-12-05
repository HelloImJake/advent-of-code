file = open("input.txt", "r")

found_pairs = 0
for line in file:
    found = False
    elf_pair = line.strip().split(",")
    current_elf = 0
    elf_pairs = []
    for elf in elf_pair:
        current_elf += 1
        range1 = int(elf.split("-")[0])
        range2 = int(elf.split("-")[1])
        ranges = list(range(range1, range2 + 1))
        elf_pairs.append(ranges)
    
    print(elf_pairs[0], elf_pairs[1])
    
    check = any(item in elf_pairs[0] for item in elf_pairs[1])
    if check is True:
        found = True
    
    check = any(item in elf_pairs[1] for item in elf_pairs[0])
    if check is True:
        found = True
    
    if found is True:
        print("full inside")
        found_pairs += 1

print(found_pairs)

