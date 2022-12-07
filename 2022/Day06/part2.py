import string
def read_input(filename):
    with open(filename, "r") as f:
        line = f.readline().strip()
        for i in range(len(line)):
            if len(set(line[i:i+14]))==14:
                return i + 14 


if __name__=="__main__":
    print(read_input("./input.txt"))
