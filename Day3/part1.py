import re

input = ""
total = 0
res = 0

with open (r"Day3/input.txt", "r") as file: 
    input = file.read().replace('\n', '')

patterns = re.findall(r'mul\((\d+),(\d+)\)', input)


for pattern in patterns:
    num1 = int(pattern[0])
    num2 = int(pattern[1])
    res += (num1*num2)

print(res) 
    
            
