def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    sum = 0
    sum_ins = 0
    for i in my_list:
        if i % 7 == 0:
            while elem in i != 0:
                a = elem % 10
                sum_ins += a
                elem // 10
                print(sum)
            sum += sum_ins
            sum_ins = 0
    print(sum)


    return sum  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    return 1  # Верните значение полученной суммы


my_list = []  # Соберите нужный список по заданию
for i in range(1, 1001):
    if i % 2 != 0:
        my_list.append(i * i * i)
print(my_list)
result_1 = sum_list_1(my_list)
print(result_1)
# result_2 = sum_list_2(my_list)
# print(result_2)

print('end')