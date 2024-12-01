values = []
left = []
right = []
result = 0

with open (r"Day1\input.txt") as file: 
    for line in (file.readlines()):
        line = line.split() 
        values.append(line)

for value in values: 
    left.append(value[0])
    right.append(value[1])

left.sort()
right.sort()

for value in left:
    similarity_count = 0
    for similarity in right:
        if value == similarity:
            similarity_count +=1 
    score = int(similarity_count) * int(value)
    if score != 0:
        result += score

print(result)
        
            