def part1():
    with open("./input") as f:
        first_line = True 
        count = 0
        for line in f.readlines():
            if first_line:
                num = int(line.strip())
                first_line = False
                continue
            else:
                new_num = int(line.strip())
                if new_num > num :
                    count += 1
                num = new_num
    return count

if __name__=="__main__":
    with open("./input_part2") as f:
        first = True 
        nums = []
        for line in f.readlines():
            nums.append(int(line.strip()))
    count = 0
    for i in range(len(nums)):
        if i ==  0:
            current_sum = sum(nums[i:i+3])
            continue
        try:
            next_sum = sum(nums[i:i+3])
            if next_sum > current_sum:
                count += 1
            current_sum = next_sum 
        except:
            pass
    print(count)

            
