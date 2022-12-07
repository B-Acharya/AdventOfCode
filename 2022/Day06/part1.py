import string
def read_input(filename):
    with open(filename, "r") as f:
        line = f.readline().strip()
        for i in range(len(line)):
            if len(set(line[i:i+4]))==4:
                return i + 4

                
    return towers, moves


if __name__=="__main__":
    print(read_input("./input.txt"))
