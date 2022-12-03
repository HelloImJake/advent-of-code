file = open("input.txt", "r")

# A = Rock
# B = Paper
# C = Scissors

# X = Rock
# Y = Paper
# Z = Scissors

def convert_value(move):
    if move == "X":
        return "A"
    elif move == "Y":
        return "B"
    elif move == "Z":
        return "C"
    
def calculate_needed(result, move):
    if result == "X": # loss needed
        if move == "A":
            return "C" # rock, return scissors
        elif move == "B":
            return "A" # paper, return rock
        elif move == "C":
            return "B" # scissors, return paper
    elif result == "Y":
        return move # return the move they gave for tie
    else:
        if move == "A":
            return "B" # rock, return paper
        elif move == "B":
            return "C" # paper, return scissors
        elif move == "C":
            return "A" # scissors, return rock

def get_score(opponent, your_move) -> int:
    #your_move = convert_value(your_move)
    print(f"Opponent went: {opponent}, you went: {your_move}")
    if opponent == your_move:
        print("tie")
        return 3
    elif your_move == "A":
        if opponent == "C":
            print("win")
            return 6
        else:
            print("loss")
            return 0
    elif your_move == "B":
        if opponent == "A":
            print("win")
            return 6
        else:
            print("loss")
            return 0
    elif your_move == "C":
        if opponent == "B":
            print("win")
            return 6
        else:
            print("loss")
            return 0


guide = []
for line in file:
    chars = line.strip().split(" ")
    guide.append(chars)

# print(guide)

score = 0
for round in guide:
    round_score = 0
    opponent = round[0]
    your_move = round[1]

    calculated_move = calculate_needed(your_move, opponent)
    print(f"Calculated Move: {calculated_move}")
    
    if calculated_move == "A":
        round_score += 1
    elif calculated_move == "B":
        round_score +=2
    else:
        round_score+=3
    
    round_score += get_score(opponent, calculated_move)
    print(round_score)
    score += round_score

print(score)

