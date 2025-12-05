from itertools import combinations


def check_valid(id: str):

    n = len(id)

    if n % 2 == 0:
        first_part = id[0 : n // 2]
        second_path = id[n // 2 :]
        if first_part == second_path:
            return False
        else:
            return True
    else:
        return True


def check_valid_v2(id: str):

    n = len(id)

    n_ind = len(set(id))

    if (n % n_ind == 0) and (n != n_ind):

        parts = [id[i : i + n_ind] for i in range(0, n, n_ind)]

        if len(parts) == 1:
            return True

        parts_uni = set(parts)
        print(parts_uni, parts)

        parts_uni.discard("")

        if len(parts_uni) == 1:
            return False
        else:
            return True

    else:
        return True


def check_valid_v3(id: str):
    n = len(id)

    for pattern_len in range(1, n):
        if n % pattern_len == 0 and n // pattern_len >= 2:
            pattern = id[:pattern_len]
            if pattern * (n // pattern_len) == id:
                return False
    return True


def read_txt(path):

    with open(path, "r") as f:

        text = f.read()

        ids = text.split(",")

        buffer = list()

        for id in ids:

            low, high = id.split("-")

            for i in range(int(low), int(high) + 1):

                if check_valid_v3(str(i)):
                    continue
                else:
                    buffer.append(i)

    print(sum(buffer))


if __name__ == "__main__":

    read_txt("./input.txt")
