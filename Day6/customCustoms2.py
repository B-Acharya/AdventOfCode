if __name__ == "__main__":
    with open('./Day6/input.txt') as f:
        groups = list()
        selections = list()
        sum = 0
        for line in f :
            if line=="\n":
                groups.append(selections)
                selections = list()
            else:
                selections.append(set(line.strip()))
    for group in groups:
        unique  = set.intersection(*group)
        sum += len(unique)
    print(sum)