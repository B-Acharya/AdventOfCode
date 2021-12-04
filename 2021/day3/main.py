def extract():
    bin_nums = []
    with open("./input") as f:
        for line in f.readlines():
            bin_nums.append(line.strip())
    return bin_nums

def part1():

    bin_nums = extract()
    print(bin_nums)
    gamma_rate = 0
    epsilon = 0
    for i in range(len(bin_nums[0])):
        ones = 0
        zeros = 0 
        for num in bin_nums:
            if num[i] == '1':
                ones += 1
            else:
                zeros += 1
        if ones> zeros:
            gamma_rate += 2**(len(bin_nums[0])-i - 1)
        else:
            epsilon += 2**(len(bin_nums[0])-i - 1)
    print(gamma_rate*epsilon)

def oxygen_filter( nums , pos):
    ones = 0
    zeros = 0
    for num in nums:
        if num[pos] == '1':
            ones += 1
        else:
            zeros += 1
    if ones>=zeros:
        return [num for num in nums if num[pos] == '1']
    else:
        return [num for num in nums if num[pos] == '0']

def co_filter( nums , pos):
    ones = 0
    zeros = 0
    for num in nums:
        if num[pos] == '1':
            ones += 1
        else:
            zeros += 1
    if zeros<=ones:
        return [num for num in nums if num[pos] == '0']
    else:
        return [num for num in nums if num[pos] == '1']



if __name__=="__main__":
    bin_nums = extract()
    nums = bin_nums.copy()
    for i in range(len(nums)):
        nums = oxygen_filter(nums, i)
        if len(nums) == 1:
            break
    ox = int(nums[0],2)
    nums = bin_nums.copy()
    for i in range(len(nums)):
        nums = co_filter(nums, i)
        if len(nums) == 1:
            break
    co = int(nums[0],2)
    print(ox*co)
        
        

            
