if __name__ == "__main__":
    count=1
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    #Open the file stored as input 
    for y_i , x_i in slopes:
        trees=0
        y=0
        i=0
        with open('./input.txt') as f:
            #to go down one line at a time
            for line in f:
                if x_i == 2:
                    if i%x_i!=0:
                        i+=1
                        continue
                    i+=1
                y = y%(len(line)-1)
                if line[y]== "#":
                    trees+=1
                #go left 3 positions
                y+=y_i
        count*= trees
    print(count)
