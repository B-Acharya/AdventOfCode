
if __name__== "__main__":
    with open('./input.txt') as f:
        valid_pass = 0
        for line in f:
           #get the split up letters 
           index , letter, word = line.split()
           count = word.count(letter[0])
           #get the left and right index
           left_index , right_index = index.split('-')
           if (word[int(left_index)-1]==letter[0]) &(word[int(right_index)-1]==letter[0]):
               continue
           elif(word[int(left_index)-1]==letter[0])|(word[int(right_index)-1]==letter[0]):
               valid_pass+=1
    print(valid_pass)