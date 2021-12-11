import numpy as np
from numpy.core.numeric import zeros_like
from collections import deque
import matplotlib.pyplot as plt
def extract():
    lines = []
    with open("D:/AdventOfCode/2021/Day11/input.txt") as f:
        for line in f.readlines():
            lines.append(list(map(int,list(line.strip()))))
    return lines 
if __name__=="__main__":
    num = np.array(extract())
    rows = [0,1,0,-1,1,-1,1,-1]
    cols = [1,0,-1,0,1,-1,-1,1]
    R = len(num)
    C = len(num)
    count = 0
    for step in range(1000):
        num += 1
        mask = num>9
        flash = [tuple(i) for i in np.argwhere(num > 9)]
        count += len(flash)
        num[mask] = 0
        for index in flash:
            for d in range(8):
                row = index[0] + rows[d]
                col = index[1] + cols[d]
                if 0<=row<R and 0<=col<C and (row,col) not in flash:
                    num[row,col] += 1
                    if num[row,col]> 9:
                        count+= 1
                        flash.append(tuple([row,col]))
                        mask[row,col] = True
                        num[row,col] = 0
        print(all(mask.ravel()),step)
print(count)


