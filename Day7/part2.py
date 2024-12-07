def convert_list_to_int_list(liste: list, ignore_zeichen='') -> list:
    """Konvertiert alle Elemente einer Liste, auch in verschachtelten Listen, zu Integern.

    Args:
      liste: Die Liste, die konvertiert werden soll.
      ignore_zeichen: Ein optionales Zeichen, das ignoriert werden soll.

    Returns:
      Eine neue Liste mit allen Elementen als Integer.
    """
    neue_liste = []
    for element in liste:
        if isinstance(element, list):
            neue_liste.append(convert_list_to_int_list(element, ignore_zeichen))
        else:
            try:
                if element != ignore_zeichen:
                    neue_liste.append(int(element))
            except ValueError:
                raise ValueError(f"Element '{element}' kann nicht in einen Integer umgewandelt werden.")
    return neue_liste

from itertools import product, chain

file_path = r'Day7/input.txt'
with open(file_path, "r") as file:
    file_content = file.read()
    
lines_full = file_content.split("\n")

file_path = r'Day7/example.txt'
with open(file_path, "r") as file:
    file_content = file.read()
    
lines_example = file_content.split("\n")

equation = [line.split(': ') for line in lines_full]
for i in equation:
    i[1] = i[1].split(' ')

equation = convert_list_to_int_list(equation)

def get_possible(charset, maxlength):
  return (''.join(candidate)
          for candidate in chain.from_iterable(product(charset, repeat=i)
          for i in range(1, maxlength + 1)))

def eval_left_to_right(e):
    t = []
    n = ""
    for c in e:
        if c.isdigit():
            n += c
        elif c in "+*":
            t.extend([int(n), c])
            n = ""
    t.append(int(n))
    r = t[0]
    for i in range(1, len(t), 2):
        r = r + t[i + 1] if t[i] == "+" else r * t[i + 1]
    return r

counter = 0

for eq in equation:
    result = eq[0]
    for poss in get_possible('*+', len(eq[1]) - 1):
        new = str(eq[1][0])
        for i in range(len(poss)):
            new += f' {poss[i]} {eq[1][i + 1]}'
        if eval_left_to_right(new) == int(result):
            counter += result
            break

print(counter)
