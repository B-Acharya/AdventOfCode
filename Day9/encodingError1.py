def validNumber(listofNums, number):
    for num in listOfNumbers:
        if (number - num ) in listOfNumbers:
            return False
    return True

def contigousSet(listOfNumbers,number):
    sum = 0
    for i in range(len(listOfNumbers)):
        sum += listOfNumbers[i]
        for j in range(i + 1 , len(listOfNumbers)):
            if sum > number:
                sum = 0
                break
            elif sum < number:
                sum += listOfNumbers[j]
            elif sum == number:
                return min(listOfNumbers[i:j]) + max(listOfNumbers[i:j])


if __name__=="__main__":
    listOfNumbers = list()
    with open("./input.txt") as f:
        for line in f:
            listOfNumbers.append(int(line))
    for i in range(len(listOfNumbers)-25):
        if validNumber(listOfNumbers[i:i+25],listOfNumbers[i+26]):
            print(listOfNumbers[i+26])
            break
    print(contigousSet(listOfNumbers,177777905))