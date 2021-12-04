def processInstruction(line):
    code, value = line.split(" ")
    return code, value

def checkTermination(commands):
    flag = True 
    i = 0
    listOfVisistedLines= list()
    while(flag):
        code , value = commands[i] 
        if code == "jmp":
            i += value
            if i in listOfVisistedLines:
                return i
            elif i == 620:
                return i
            listOfVisistedLines.append(i) 
            continue
        elif code == "acc":
            listOfVisistedLines.append(i) 
            i+=1
            continue
        listOfVisistedLines.append(i) 
        i+=1
        if i == 620:
            return i  
        elif i ==621:
            return i


def calAccumulater(commands):
    flag = True 
    i = 0
    acc = 0
    listOfVisistedLines= list()
    while(flag):
        if i == 621:
            return acc
        code , value = commands[i] 
        if code == "jmp":
            i += value
            if i in listOfVisistedLines:
                return acc
            listOfVisistedLines.append(i) 
            continue
        elif code == "acc":
            acc += value
            listOfVisistedLines.append(i) 
            i+=1
            continue
        listOfVisistedLines.append(i) 
        if i == 620:
            return acc
        i+=1
        
if __name__=="__main__":
    commands = dict()
    with open("./input.txt") as f:
        for i, line in enumerate(f):
            code , value = processInstruction(line)
            commands[i] = (code, int(value))
    #print(calAccumulater(commands))
    for i in range(620):
        commands_1 = commands.copy()
        if  commands[i][0] == "jmp":
            commands_1[i] =  ("nop", commands[i][1])
            value = checkTermination(commands_1)
            if (value==620):
               break
    print(calAccumulater(commands_1))