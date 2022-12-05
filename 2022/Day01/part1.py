
def read_input(filepath):
    elfs = []
    with open(filepath, "r") as f:
        total = 0
        for line in f.readlines():
            if line =="\n":
                elfs.append(total)
                total = 0
            else:
                total += int(line)
    return elfs


if __name__=="__main__":
    elfs = read_input("./input.txt")
    print(max(elfs))
    

