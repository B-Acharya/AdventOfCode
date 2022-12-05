import string
def read_input(filename):
    towers = []
    moves = []
    cond = True
    with open(filename, "r") as f:
        for line in f.readlines():
            if line == "\n":
                cond = False
                continue
            if cond:
               towers.append(line.strip("\n")) 
            else:
                moves.append(line.strip("\n"))
                
    return towers, moves


if __name__=="__main__":
    towers, moves = read_input("./input.txt") 
    tower_names = towers[-1]
    tower_dict = {}
    #filter the tower input
    for n in range(1, 10):
        index = tower_names.index(str(n))
        tower_dict[str(n)] = []
        for tower in towers[:-1]:
            if tower[index] == " ":
                continue
            else:
                tower_dict[str(n)].append(tower[index])
    for move in moves:
        move = move.split(" ")
        blocks = int(move[1])
        f = move[3]
        t = move[5]
        temp = tower_dict[f][:blocks]
        for _ in range(blocks):
            tower_dict[f].pop(0)
        tower_dict[t] = temp + tower_dict[t]
    word = ""
    for key in tower_dict.keys():
        print(key, tower_dict[key])
        word += tower_dict[key][0]
    print(word)

    
