import string
def read_input(filepath):
    with open(filepath, "r") as f:
        stratergy = []
        i = 1
        group = [] 
        for line in f.readlines():
            group.append(set(line.strip()))
            if  i % 3 ==0:
                stratergy.append(group)
                group= [] 
            i+=1
    return stratergy 


if __name__=="__main__":
    
    stratergy = read_input("./input.txt")
    total = 0 
    points = { char:point for char, point in zip(string.ascii_lowercase + string.ascii_uppercase, range(1,53))}
    for a, b, c in stratergy:
        comman = "".join(a & b & c)
        total += points[comman]
    print(total)
