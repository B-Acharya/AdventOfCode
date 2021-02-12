import pprint
import re
def processline(lineInput):
    firstBag, includedBags = lineInput.split("contain")
    firstBag = re.findall("[a-zA-Z0-9_\s]* bag",firstBag)
    if includedBags==" no other bags":
        return firstBag[0][0:-4], includedBags
    includedBags = includedBags.strip(".").split(",")
    finalDict = dict()
    for bags in includedBags:
        bags = re.findall("[a-zA-Z0-9_\s]* bag",bags)
        finalDict[bags[0][3:-4]]=bags[0][1]
    return firstBag[0][0:-4], finalDict

def countCal(currentbag, bags):
    #check if the current bag can contain other bags
    if currentbag in bags.keys():
    #check if the bag contains the shiny bag if yes done return true
        if "shiny gold" in bags[currentbag].keys():
            return True
        else :
            #iterate through all the inner bags a inital bag to check if that can contain a shiny bag
            for bag in bags[currentbag].keys():
                #if call the same fuction to check if it is true 
                if countCal(bag, bags):
                    return True
    else:
        return False

if __name__=="__main__":
    with open("./input.txt") as f:
        bags= dict()
        count = 0
        listOfBags = list()
        for line in f:
            firstbag, includedBags = processline(line.strip())
            bags[firstbag] = includedBags
    for bag in bags.keys():
        if countCal(bag,bags):
            count+=1
    print(count)