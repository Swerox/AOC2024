'''
IF IT IS DECREASING BY 1 OR 2 SAFE
IF A % B IS 1,2 OR 3 ITS SAFE
ELSE ITS UNSAFE
IF ITS DECREASING ANDDDD INCREASING ITS UNSAFE

FIRST TWO: 
87 90 92 95 96 93
12 15 16 17 17

'''

input = []
safe = 0 
count = 0
safe_packs = []

def get_de_or_in(a, b):
    if a > b:
        if a - b in {1,2,3}:
            return True
    if b > a: 
        if b - a in {1,2,3}:
            return True
    if a == b:
        return False


def is_monotonic(lst):

    increasing = all(int(lst[i]) < int(lst[i + 1]) for i in range(len(lst) - 1))
    decreasing = all(int(lst[i]) > int(lst[i + 1]) for i in range(len(lst) - 1))

    return increasing or decreasing
    
    
with open (r"Day2/input.txt") as file: 
    for line in (file.readlines()):
        line = line.split() 
        input.append(line)
        

for pack in input:
    if is_monotonic(pack):
        safe = all(get_de_or_in(int(pack[i]), int(pack[i + 1])) for i in range(len(pack) -1))
        if safe:
            print(f"SAVE: {pack}")
            count += 1
        if not safe:
            print(f"NOT SAVE CAUSE NOT IN 1..3 {pack}")
             
    else:
        print(f"NOT SAVE CAUSE NOT INCREASING OR DECREASING {pack}")

print(count)
