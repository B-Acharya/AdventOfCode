def joltage(adapters):
    jolt_1 = 0
    jolt_3 = 0
    current_jolt = 0 
    adapters.sort(reverse=True)
    for i in range(len(adapters)):
        jolt = adapters.pop()
        difference = jolt - current_jolt
        if difference == 1:
            jolt_1+=1
        elif difference ==3:
            jolt_3+=1
        current_jolt = jolt
    return jolt_1*jolt_3


        
if __name__=="__main__":
    adapters = list()
    with open("./input.txt") as f :
        for line in f:
            adapters.append(int(line))
    #adding the inbult joltage 
    adapters.append(max(adapters)+3)
    print(joltage(adapters))