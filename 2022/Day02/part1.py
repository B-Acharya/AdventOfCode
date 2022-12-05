
def read_input(filepath):
    with open(filepath, "r") as f:
        total = 0
        stratergy = []
        for line in f.readlines():
            a, b = line.strip().split(" ")

            if b == "X":
                b = "A"
            elif b == "Y":
                b = "B"
            elif b == "Z":
                b = "C"

            stratergy.append((a,b))
    return stratergy 

def rps(a,b):
    if a == "A":
        if b == "B":
            return False
        else:
            return True
    if a=="B":
        if b == "C":
            return False
        else:
            return True
    if a =="C":
        if b =="A":
            return False
        else:
            return True


if __name__=="__main__":
    
    stratergy = read_input("./input.txt")
    points = {"A":1, "B":2, "C":3}
    total = 0
    for a, b in stratergy:
        if a == b:
            total += 3 + points[b]
            continue
        if rps(b, a):
            total += 6 + points[b]
        else: 
            total += points[b]
            
    print(total)
        

    

