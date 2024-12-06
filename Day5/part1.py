from input import data

def extract_rules(data:list):
    res = []
    for line in data:
        if '|' in line:
            res.append(line.split('|'))
    return res

def extract_pages(data:list):
    res = []
    for line in data:
        if ',' in line:
            res.append([int(x) for x in line.split(',')])
    return res

def check_rules(data, rules):
    for rule in rules:
        if int(rule[0]) in data and int(rule[1]) in data:
            if data.index(int(rule[0])) > data.index(int(rule[1])):
                return False
    return True

def get_right(pages, rules):
    res = []
    for page in pages:
        if check_rules(page, rules):
           res.append(page)
    return res

data1 = data.split('\n')

rules = extract_rules(data1)
pages = extract_pages(data1)

correct_updates = get_right(pages, rules)

middle_pages_sum = 0
for update in correct_updates:
    middle_index = len(update) // 2
    middle_pages_sum += update[middle_index]

print(middle_pages_sum)