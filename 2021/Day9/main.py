import numpy as np
from numpy.core.numeric import zeros_like
from collections import deque
import matplotlib.pyplot as plt
def extract():
    strings = []
    with open("D:/AdventOfCode/2021/Day9/input.txt") as f:
        for line in f.readlines():
            strings.append(list(map(int,list(line.strip()))))
    return strings

def row_low(row):

    mask = np.zeros_like(row)
    for i in range(len(row)):
        if i == 0 :
            if row[i]<row[i+1]:
                mask[i] = 1
        elif i == len(row)- 1 :
            if row[i-1] > row[i]:
                mask[i] = 1 
        else:
            if row[i-1]>row[i] and row[i] < row[i+1]:
                mask[i] = 1
    return mask

if __name__=="__main__":
    data = extract()
    # mask_row = zeros_like(strings)
    # for rows  
    # for i, row in enumerate(strings):
        # mask_row[i] = row_low(row)
    # mask_col = zeros_like(strings)
    # for col
    # for i, row in enumerate(strings.T):
        # mask_col[i] = row_low(row)
    # mask = mask_row + mask_col.T
    # mask = mask{}
    # print(sum(strings[mask==2]+1))
    # for 
    R = len(data)
    C = len(data[0])
    row = [-1,0,1,0]
    col = [0,-1,0,1]
    ans = 0
    for i in range(R) :
        for j in range(C):
            flag = True
            for point in range(4):
                r = i + row[point]
                c = j + col[point]
                if 0<=r< R and 0<=c<C and data[r][c]<=data[i][j]:
                    flag = False
            if flag:
                ans += data[i][j] + 1
    matplot
    print(ans)
    S = []
    SEEN = set()
    for r in range(R):
        for c in range(C):
            if (r,c) not in SEEN and data[r][c]!=9:
                size = 0
                Q = deque()
                Q.append((r,c))
                while Q:
                    (r,c) = Q.popleft()
                    if (r,c) in SEEN:
                        continue
                    SEEN.add((r,c))
                    size += 1
                    for d in range(4):
                        rr = r+row[d]
                        cc = c+col[d]
                        if 0<=rr<R and 0<=cc<C and data[rr][cc]!=9:
                            Q.append((rr,cc))
                S.append(size)
    S.sort()
    print(S[-1]*S[-2]*S[-3])
