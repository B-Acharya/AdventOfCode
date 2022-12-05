
def read_input(filepath):
    with open(filepath, "r") as f:
        total = 0
        stratergy = []
        for line in f.readlines():
            a, b = line.strip().split(" ")

            stratergy.append((a,b))
    return stratergy 


if __name__=="__main__":
    
    stratergy = read_input("./input.txt")
    points = {"A":1, "B":2, "C":3}

    win_dict = {"A":"B","B":"C","C":"A"}
    lose_dict = {"A":"C","B":"A","C":"B"}
    total = 0
    for a, b in stratergy:
        if b == "X":
            total += points[lose_dict[a]]
        elif b == "Y":
            total += 3 + points[a]
        else:
            total += 6 + points[win_dict[a]]

    print(total)
        

    

