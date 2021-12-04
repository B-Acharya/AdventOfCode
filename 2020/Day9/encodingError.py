def validNumber(listofNums, number):
    for num in listOfNumbers:
        if (number - num ) in listOfNumbers:
            return False
    return True

if __name__=="__main__":
    listOfNumbers = list()
    with open("./input.txt") as f:
        for line in f:
            listOfNumbers.append(int(line))
    for i in range(len(listOfNumbers)-25):
        if validNumber(listOfNumbers[i:i+25],listOfNumbers[i+26]):
            print(listOfNumbers[i+26])
            break