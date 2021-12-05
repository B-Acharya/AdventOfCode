import numpy as np
def extract():
    points = []
    with open("D:/AdventOfCode/2021/day5/input.txt") as f:
        for line in f.readlines():
            point1 , point2 = line.split("->")
            points.append([tuple(map(int,(point1.strip().split(',')))), tuple(map(int,(point2.strip().split(','))))])
    return points        

if __name__=="__main__":

    points = extract()
    board = np.zeros(shape=(1000,1000))
    for point in points:
        x0, y0 = point[0]
        x1, y1 = point[1]
        if x0 == x1:
            if y0 < y1:
                board[x0,y0:y1 +1] += 1
            else:
                board[x0,y1:y0 +1] += 1
        elif y0 == y1:
            if x0 < x1:
                board[x0:x1+1,y0] += 1
            else:
                board[x1:x0+1,y0] += 1
        elif x0<x1:
            if y0<y1:
                for i in range(y1-y0+1):
                    board[x0+i,y0+i] += 1
            elif y0>y1:
                for i in range(y0-y1+1):
                    board[x0+i,y0-i] += 1
        elif x1<x0:
            if y0<y1:
                for i in range(y1-y0+1):
                    board[x0-i,y0+i] += 1
            elif y0>y1:
                for i in range(y0-y1+1):
                    board[x0-i,y0-i] += 1

    num = board[board>=2]
    print(num.shape)