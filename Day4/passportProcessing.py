if __name__ == "__main__":
    #Open the file stored as input 
    listOfValid = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    listOfValid1 = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    listOfValid.sort()
    listOfValid1.sort()
    listOfPassports = list()
    valid = 0
    passPort = dict()
    with open('./Day4/input.txt') as f:
        for line in f :
            if line=="\n":
                listOfPassports.append(passPort)
                passPort = dict()
                continue
            else:
                for attributes in line.split():
                    key , values = attributes.split(":")
                    passPort[key]= values
    for dicts in listOfPassports:
        checkList = list(dicts.keys())
        checkList.sort()
        if (listOfValid == checkList) | (listOfValid1==checkList):
            valid+=1
    print(valid)