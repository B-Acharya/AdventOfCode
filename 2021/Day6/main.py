import numpy as np
import collections
def extract():
    with open("D:/AdventOfCode/2021/Day6/input.txt") as f:
        nums = list(map(int, f.read().strip().split(",")))
    return nums


if __name__=="__main__":
    # puff solution works for part1 and not for part2 
    # # nums = np.array(extract(), dtype="ushort")
    # nums = np.array([3,4,3,1,2], dtype="ushort")
    # days = 18
    # print(nums)
    # for i in range(0,days):
    #     index = np.array(nums==0, dtype="bool")
    #     nums[index] = 6
    #     nums[~index] -=1
    #     noNewFish = nums[index].shape[0]
    #     nums = np.append(nums, np.full(shape=noNewFish, fill_value=8, dtype="ushort")) 
    #     print(i)
    # print(nums.shape)

    # lets try something better inspired from reddit
    c = collections.Counter()
    days = 256
    c.update(extract())
    print(c)
    counter = {n: c[n] for n in range(-1,9)}
    for _ in range(days):
        # increa
        counter = {n: counter[n+1] for n in range(-1, 8)}
        counter[8] = counter[-1]
        counter[6] += counter[-1]
        counter[-1] = 0
    print(sum(counter.values()))


