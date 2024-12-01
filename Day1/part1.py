values = []
left = []
right = []
result = 0

def get_difference(a, b):
    if a > b: 
        return a-b 
    if a < b: 
        return b-a
    if a == b: 
        return 0

with open ("Day1\input.txt") as file: 
    for line in (file.readlines()):
        line = line.split() 
        values.append(line)


for value in values: 
    left.append(value[0])
    right.append(value[1])

left.sort()
right.sort()

for index in range(len(left)):
    difference = get_difference(int(left[index]), int(right[index]))
    result += difference

print(result)

