import numpy as np
from numpy.core.numeric import zeros_like
from collections import deque
import matplotlib.pyplot as plt
def extract():
    strings = []
    with open("D:/AdventOfCode/2021/Day10/input.txt") as f:
        for line in f.readlines():
            strings.append(list(line.strip()))
    return strings
if __name__=="__main__":
    opening = ['[','{','(','<']
    closing = [']','}',')','>']
    data = extract()
    syntax = 0 
    points = {')':3,']':57,'}':1197,'>':25137}
    autocomplete = {'(':1,'[':2,'{':3,'<':4}
    new_list = []
    for line in data:
        queue = []
        for char in line:
            if char in opening:
                queue.append(char)
            else:
                if closing.index(char) == opening.index(queue[-1]):
                    queue.pop()
                else:
                    syntax += points[char]
                    break
        else:
            # print(queue)
            new_list.append(queue)
    all_total = []
    for line in new_list:
        total = 0
        for letter in line[::-1]:
            total*=5
            total+= autocomplete[letter]
        all_total.append(total)
    all_total.sort()
    print(all_total[len(all_total)//2 ])
    print(syntax)
      



