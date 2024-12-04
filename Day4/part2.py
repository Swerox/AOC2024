import re2
from input import data

data = data.replace("\n", "")

# part 1
patterns = ["XMAS", "X...\n.M..\n..A.\n...S"]
print(sum(len(re2.findall(pattern, data, rotate=True)) for pattern in patterns))

# part 2
print(len(re2.findall("M.M\n.A.\nS.S", data, rotate=True)))