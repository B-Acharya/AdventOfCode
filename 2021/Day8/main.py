def extract():
    strings = []
    with open("D:/AdventOfCode/2021/Day8/input.txt") as f:
        for line in f.readlines():
            strings.append(line.strip().split(' | '))

    return strings

def mapping(string):
    mappings = {i: 0 for i in range(10)}
    for word in string.split():
        if len(word) == 4:
            mappings[4] = word
        elif len(word) == 2:
            mappings[1] = word
        elif len(word) == 3:
            mappings[7] = word
        elif len(word) == 7:
            mappings[8] = word
    for word in string.split():
        if len(word) == 6:
            if set(mappings[4]).issubset(set(word)):
                # is 6 or 9
                    mappings[9] = word
            else:
                if set(mappings[1]).issubset(set(word)):
                    mappings[0] = word
                else:
                    mappings[6] = word
    for word in string.split():
        if len(word) == 5:
            if set(mappings[1]).issubset(set(word)):
                mappings[3] = word
            else:
                if set(word).issubset(set(mappings[9])):
                    mappings[5] = word
                else:
                    mappings[2] = word

    return mappings
if __name__=="__main__":
    strings = extract()
    count = 0
    for string in strings:
        # print(string[1].split())
        length = list(map(len, string[1].split() ))
        for i in length:
            if i == 2:
                count += 1
            elif i == 4:
                count += 1
            elif i == 3:
                count += 1
            elif i == 7:
                count += 1
    #part 2
    total = []
    for string in strings:
        mappings = mapping(string[0])
        # reverse mappings
        mappings = {''.join(sorted(value)):key for key, value in mappings.items()}
        print(mappings)
        num = []
        for string in string[1].split():
            value = mappings[''.join(sorted(string))]
            num += str(value)
        print(num)
        total.append(int("".join(num)))
    print(sum(total))
            


