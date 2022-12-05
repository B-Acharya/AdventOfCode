import string
def read_input(filepath):
    with open(filepath, "r") as f:
        stratergy = []
        for line in f.readlines():
            rucksack = line.strip()
            l = len(rucksack)
            if l%2!=0:
                print("fucked")
            c1 = rucksack[0:l//2]
            c2 = rucksack[l//2:]

            stratergy.append((c1,c2))
    return stratergy 


if __name__=="__main__":
    
    stratergy = read_input("./input.txt")
    total = 0 
    points = { char:point for char, point in zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53))}
    for c1, c2 in stratergy:
        common = "".join(set(c1).intersection(c2))
        total += points[common]
    print(total)
