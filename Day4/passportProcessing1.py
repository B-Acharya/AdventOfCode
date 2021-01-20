import re
def validPassport(passportDict):
    if not ((int(passportDict["byr"])>=1920) & (int(passportDict["byr"])<=2002)):
        return False 
    if not ((int(passportDict["iyr"])>=2010) & (int(passportDict["iyr"])<=2020)):
        return False 
    if not ((int(passportDict["eyr"])>=2020) & (int(passportDict["eyr"])<=2030)):
        return False 
    if passportDict["hgt"].find("in") != -1:
        index = passportDict["hgt"].find("in")
        if not ((int(passportDict["hgt"][0:index]) >= 59) & (int(passportDict["hgt"][0:index]) <= 76)):
            return False
    if passportDict["hgt"].find("cm") != -1:
        index = passportDict["hgt"].find("cm")
        if not ((int(passportDict["hgt"][0:index]) >= 150) & (int(passportDict["hgt"][0:index]) <= 193)):
            return False
    if passportDict["hgt"].find("in") == -1 and passportDict["hgt"].find("cm") == -1:
        return False
    if not (re.search('#[0-9a-f]{6}',passportDict["hcl"])):
        return False
    contents = ["amb","blu","brn","gry","grn","hzl","oth"]
    if passportDict["ecl"] not in contents:
        return False
    if not (re.search("^[0-9]{9}$",passportDict["pid"])):
        return False
    else:
        return True

if __name__ == "__main__":
    #Open the file stored as input 
    listOfValid = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    listOfValid1 = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    listOfValid.sort()
    listOfValid1.sort()
    listOfPassports = list()
    valid = 0
    passPort = dict()
    with open('./input.txt') as f:
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
            if validPassport(dicts):
                valid+=1
    print(validPassport({"pid":"012187499", "hgt":"74in", "ecl":"grnl", "iyr":"2012", "eyr":"2030", "byr":"1980", "hcl":"#62aa3f"}))
    print(valid)