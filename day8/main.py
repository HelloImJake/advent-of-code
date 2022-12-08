from functools import reduce
file = open("input.txt", "r")

def checkVertical(grid, x, y, type):
    trees = []
    starting = 0
    ending = x
    if type == "below":
        starting = x+1
        ending = len(grid)
    for x_loc in range(starting, ending):
        trees.append(grid[x_loc][y])
        #print(f"Found Tree! : {grid[x_loc][y]}")
    return trees

def checkHorizontal(grid, x, y, type):
    trees = []
    starting = 0
    ending = y
    if type == "after":
        starting = y+1
        ending = len(grid[x])
    for y_loc in range(starting, ending):
        trees.append(grid[x][y_loc])
        #print(f"Found Tree! : {grid[x][y_loc]}")
    return trees

def isVisible(grid, x, y):
    visibility = []
    visibility.append(checkVertical(grid, x, y, "above"))
    visibility.append(checkVertical(grid, x, y, "below"))
    visibility.append(checkHorizontal(grid, x, y, "before"))
    visibility.append(checkHorizontal(grid, x, y, "after"))
    print(visibility)

def calcScore(grid, x, y):
    visibility = []
    visibility.append(reversed(checkVertical(grid, x, y, "above")))
    visibility.append(checkVertical(grid, x, y, "below"))
    visibility.append(reversed(checkHorizontal(grid, x, y, "before")))
    visibility.append(checkHorizontal(grid, x, y, "after"))

    scores = []
    for direction in visibility:
        score = 0
        for tree in direction:
            score += 1
            if tree >= grid[x][y]:
                break
        scores.append(score)
    total_score = reduce(lambda x, y: x*y, scores)
    return total_score

grid = []
for line in file:
    row = []
    row[:0] = line.strip()
    grid.append(row)

# above = reversed(checkVertical(grid, x, y, "above"))
# below = checkVertical(grid, x, y, "below")
# left = reversed(checkHorizontal(grid, x, y, "before"))
# right = checkHorizontal(grid, x, y, "after")

# isVisible(grid, 1, 2)

current_highest = 0
for index, row in enumerate(grid):
    for index2, tree in enumerate(row):
        print(f"Checking Tree: {index} {index2}")
        score = calcScore(grid, int(index), int(index2))
        if score > current_highest:
            current_highest = score

print(current_highest)

