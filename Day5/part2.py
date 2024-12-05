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

def order_update(update, rules):
    ordered_update = []
    update = update.copy()  # Create a copy to avoid modifying the original list
    while update:
        for page in update:
            can_add = True
            for rule in rules:
                if int(rule[1]) == page and int(rule[0]) in update:
                    can_add = False
                    break
            if can_add:
                ordered_update.append(page)
                update.remove(page)
                break
    return ordered_update

data1 = data.split('\n')

rules = extract_rules(data1)
pages = extract_pages(data1)

incorrect_updates = []
for page in pages:
    if not check_rules(page, rules):
        incorrect_updates.append(page)

middle_pages_sum = 0
for update in incorrect_updates:
    ordered_update = order_update(update, rules)
    middle_index = len(ordered_update) // 2
    middle_pages_sum += ordered_update[middle_index]

print(middle_pages_sum)