def part1():
    plan = []
    with open("./input2") as f:
        for line in f.readlines():
            plan.append(line.split())
    return plan 

if __name__=="__main__":
#    plan = part1()
#    forward = 0
#    dept = 0
#    for direction, force in plan:
#        if direction=='forward':
#            forward += int(force)
#        elif direction == 'up':
#            dept -= int(force)
#        elif direction == 'down':
#            dept += int(force)
#
    plan = part1()
    forward = 0
    dept = 0
    aim = 0 
    for direction, force in plan:
        if direction=='forward':
            forward += int(force)
            dept += aim*int(force)
        elif direction == 'up':
            aim -= int(force)
        elif direction == 'down':
            aim += int(force)
    print( forward*dept) 
            
