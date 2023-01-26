def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    names = []
    for elem in list_in:
        elem_1 = elem.split(' ')
        names.append(elem_1[-1])
    names_str = ' '.join(names)
    names_str_little = names_str.lower()
    names_str_little_2 = names_str_little.title()
    names_final = list(names_str_little_2.split(' '))
    list_out = []
    for i in names_final:
        list_out.append(f'Привет {i} !')

    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)