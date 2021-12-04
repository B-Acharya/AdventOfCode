if __name__== "__main__":
    with open('./input.txt') as f:
        valid_pass = 0
        for line in f:
           length , letter, word = line.split()
           count = word.count(letter[0])
           left , right = length.split('-')
           if (count>=int(left)) & (count<=int(right)):
                valid_pass+=1
    print(valid_pass)