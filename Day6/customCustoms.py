if __name__ == "__main__":
    with open('./Day6/input.txt') as f:
        selections = list()
        sum = 0
        for line in f :
            if line=="\n":
                sum += len(selections)
                selections = list()
            else:
                for letter in line:
                    if (letter in selections)| (letter == "\n"):
                        continue
                    else :
                        selections.append(letter)
        print(sum)