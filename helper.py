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
def convert_list_to_matrix_list_horizontally(liste:list, seperator=" "):
    '''
    Converts list to a matrix table horizontally
    :param liste: list
    :param seperator: seperator between each element
    :return: converted list to horizontally matrix
    '''
    if not seperator:
        print('seperator cant be empty (l. 12 - helper)')

    new_list = []
    for item in liste:
        new_list.append(item.split(seperator))
    return new_list

def convert_list_to_matrix_list_vertically(liste, seperator=" ", placeholder=''):
    '''
    Converts list to a matrix table vertically
    :param placeholder: when one item extends range of others this will be placed
    :param liste: list
    :param seperator: seperator between each element
    :return: converted list to vertically matrix
    '''

    if not seperator:
        print('seperator cant be empty (l. 28 - helper)')

    liste = convert_list_to_matrix_list_horizontally(liste, seperator=seperator)
    new_list = []
    for i in range(len(liste[get_longest_list_index_inside_list(liste)])):
        temp_list = []

        for item in liste:
            if not i > len(item) - 1:
                temp_list.append(item[i])
            else:
                temp_list.append(placeholder)
        new_list.append(temp_list)
        temp_list = []

    return new_list

def get_longest_list_index_inside_list(liste):
    max = 0
    max_index = 0
    for index, item in enumerate(liste):
        if len(item) > max:
            max = len(item)
            max_index = index
    return max_index