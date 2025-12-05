class dial:

    def __init__(self):

        self.current: int = 50
        self.zero_counter = 0
        self.MIN = 0
        self.MAX = 100

    def update_current(self, rotation: str):

        if rotation[0] == "L":

            self.left_rotate(int(rotation[1:]))

        elif rotation[0] == "R":

            self.right_rotate(int(rotation[1:]))

        else:
            raise ValueError

        return self.current

    def left_rotate(self, num: int):

        new_position = self.current - num

        if new_position < 0:
            self.zero_counter += (self.current // self.MAX) - (new_position // self.MAX)
        # if self.current < 0:
        #    self.zero_counter += (abs(self.current) - 1) // self.MAX

        # self.zero_counter += (self.current - num) // self.MAX
        self.current = ((new_position % self.MAX) + self.MAX) % self.MAX

    def right_rotate(self, num: int):

        new_position = self.current + num
        self.zero_counter += (new_position // self.MAX) - (self.current // self.MAX)
        # self.zero_counter += self.current // self.MAX

        self.current = new_position % self.MAX


def counter(current, rotation):

    if rotation[0] == "L":

        # print(current, rotation[1:])
        new = current - int(rotation[1:])

        if new < 0:
            return counter(100, f"L{abs(new)}")

        else:
            return new

    elif rotation[0] == "R":

        new = current + int(rotation[1:])

        new = new % 100

        return new


def read_txt(path):

    with open(path, "r") as f:

        dail_inst = dial()
        zero_count = 0
        count = 50

        for line in f.readlines():

            count = dail_inst.update_current(line)
            # count = counter(count, line)
            # print(line, count)

            if count == 0:
                zero_count += 1

    print(zero_count, dail_inst.zero_counter)
    print(zero_count + dail_inst.zero_counter)


if __name__ == "__main__":

    read_txt("./input.txt")
    read_txt("./dummy_input.txt")
