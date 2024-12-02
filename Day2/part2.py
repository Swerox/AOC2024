input = []
safe = 0
count = 0
safe_packs = []


def get_de_or_in(a, b):
    if a > b:
        if a - b in {1, 2, 3}:
            return True
    if b > a:
        if b - a in {1, 2, 3}:
            return True
    return False


def is_monotonic(lst):
    increasing = all(int(lst[i]) < int(lst[i + 1]) for i in range(len(lst) - 1))
    decreasing = all(int(lst[i]) > int(lst[i + 1]) for i in range(len(lst) - 1))
    return increasing or decreasing


def is_safe(pack):
    if is_monotonic(pack) and all(get_de_or_in(int(pack[i]), int(pack[i + 1])) for i in range(len(pack) - 1)):
        return True

    for i in range(len(pack)):
        reduced_pack = pack[:i] + pack[i + 1:]
        if is_monotonic(reduced_pack) and all(get_de_or_in(int(reduced_pack[j]), int(reduced_pack[j + 1])) for j in range(len(reduced_pack) - 1)):
            return True

    return False


with open(r"Day2/input.txt") as file:
    for line in file.readlines():
        line = line.split()
        input.append(line)

for pack in input:
    if is_safe(pack):
        print(f"SAFE: {pack}")
        count += 1
    else:
        print(f"NOT SAFE: {pack}")

print(f"Total SAFE reports: {count}")
