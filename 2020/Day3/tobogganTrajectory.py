if __name__ == "__main__":
    y = 0
    trees= 0
    #Open the file stored as input 
    with open('./input.txt') as f:
        #to go down one line at a time
        for line in f:
            y = y%(len(line)-1)
            if line[y]== "#":
                trees+=1
            #go left 3 positions
            y+=3
    print(trees)
