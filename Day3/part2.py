from input import data
import re

data = data.replace("\n", "")

enabled = True
res = 0

patterns = re.split(r"(\bdo\(\)|\bdon't\(\))", data) 
for pattern in patterns:
    pattern = pattern.strip()
    if pattern == "do()":
        enabled = True  
    elif pattern == "don't()":
        enabled = False
    elif enabled:
        patterns = re.findall(r"mul\((\d+),(\d+)\)", pattern)
        for pattern in patterns:
            num1 = int(pattern[0])
            num2 = int(pattern[1])
            res += num1 * num2

print(res)
