import numpy as np
def extract():
    boards = []
    with open("input") as f:
        first_line = True
        lines = f.read() 
    lines = lines.split('\n\n')
    random_numbers = list(map(int, lines[0].split(',')))
    for board in lines[1:]:
        bingo = []
        temp = board.strip().split("\n")
        for row in temp:
            bingo.append(list(map(int, row.split())))
        boards.append(np.array(bingo))

    return random_numbers, boards

def col_win(board, numbers):

    mask = np.isin(board, numbers)
    flag = 0 
    for i in range(5):
        if all(mask[:,i]):
            flag += 1 
    if flag == 1:
        return True

    return False

def row_win(board, numbers):
    mask = np.isin(board, numbers)
    flag = 0 
    for i in range(5):
        if all(mask[i,:]):
            flag += 1 
    if flag == 1:
        return True
    return False
        

if __name__=="__main__":
    random_numbers, boards = extract()
    wining_board = []
    for i in range(len(random_numbers)):
        nums = random_numbers[:i] 
        for j, board in enumerate(boards):
            if col_win(board, nums) or  row_win(board, nums):
                wining_board.append((boards.pop(j), nums))
        else:
            continue
        # for the second task and cache all the wining boards
    #print(board, nums)
    #mask = np.isin(board, nums)
    #output_board = board[~mask]
    #print(sum(output_board)* nums[-1])
    board , num = wining_board[-1]
    mask = np.isin(board, num)
    print(mask)
    output_board = board[~mask]
    print(output_board)
    print(sum(output_board)*num[-1])
