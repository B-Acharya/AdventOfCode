import numpy as np
from typing import List


def joltage(bank: List[int]):

    print(bank)

    start_index = np.argmax(bank)

    if start_index == len(bank) - 1:
        end_index = np.argmax(bank[:-1])
        start_digit = bank[:-1][end_index]
        end_digit = bank[start_index]
    else:
        end_index = np.argmax(bank[start_index + 1 :])

        start_digit = bank[start_index]
        end_digit = bank[start_index + 1 :][end_index]

    print(start_digit, end_digit)
    print("-------")

    return int(str(start_digit) + str(end_digit))


def read_txt(path):

    banks = []
    jolt = 0

    with open(path, "r") as f:

        for line in f.readlines():

            bank = []
            for i in line.strip("\n"):
                bank.append(int(i))
            jolt += joltage(bank)

    print(jolt)


if __name__ == "__main__":

    read_txt("./input.txt")
