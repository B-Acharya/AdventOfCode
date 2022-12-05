import string
def compare(a,b):
    a1, a2 = map(int,a.split("-"))
    b1, b2 = map(int,b.split("-"))
    if (b1 <= a1 <=b2) or (b1<= a2 <=b2):
        return True
    elif (a1 <= b1 <=a2) or (a1<= b2 <=a2): 
        return True
    else: 
        return False

    
def read_input(filepath):
    with open(filepath, "r") as f:
        total = 0
        for line in f.readlines():
            a, b = line.strip().split(",")
            if compare(a,b):
                total += 1
    print(total)



if __name__=="__main__":
    
    stratergy = read_input("./input.txt")
