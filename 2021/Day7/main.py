
import numpy as np
def extract():
    with open("D:/AdventOfCode/2021/Day7/input.txt") as f:
        nums = list(map(int, f.read().strip().split(",")))
    return nums

def sum_part_two(num):
    total = 0
    for i in range(1, num+1):
        total+=i
    return total

if __name__=="__main__":
    nums = np.array(extract())
    # nums = np.array([16,1,2,0,4,2,7,1,2,14])
    max_pos = max(nums)
    best = np.inf
    for pos in range(max_pos):
        total = np.sum(list(map(sum_part_two, np.abs(nums - pos))))
        if total < best:
            best = total
    print(best)


