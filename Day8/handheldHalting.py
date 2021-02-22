def processInstruction(line):
    code, value = line.split(" ")
    return code, value

def calAccumulater(commands):
    flag = True 
    i = 0
    acc = 0
    listOfVisistedLines= list()
    while(flag):
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
        else:
            listOfVisistedLines.append(i) 
            i+=1

        
if __name__=="__main__":
    commands = dict()
    with open("./input.txt") as f:
        for i, line in enumerate(f):
            code , value = processInstruction(line)
            commands[i] = (code, int(value))
    print(calAccumulater(commands))
            