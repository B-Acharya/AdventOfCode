import numpy as np

if __name__ == '__main__':
    with open('./adventcode') as f:
        read_data = f.read().rstrip().splitlines()
        for num in read_data:
            for num1 in read_data:
                for num2 in read_data:
                    if (int(num2) + int(num) + int(num1)) == 2020:
                            print(int(num)*int(num1)*int(num2))
                            break


