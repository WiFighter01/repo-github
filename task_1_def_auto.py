def auto(n):
    '''
    Задача:
    Автомат обрабатывает натуральное число N по следующему алгоритму:
    1. Строится двоичная запись числа N.
    2. Складываются все цифры полученной двоичной записи. В конце записи (справа)
    дописывается остаток от деления суммы на 2.
    3. Предыдущий пункт повторяется для записи с добавленной цифрой.
    4. Результат переводится в десятичную систему и выводится на экран.
    '''
    n_second = bin(n)[2:]
    b = [int(i) for i in n_second]
    summ = 0
    for i in b:
        summ += i
    b.append(summ % 2)
    summ = 0
    for i in b:
        summ += i
    b.append(summ % 2)

    return int(''.join([str(i) for i in b]), 2)


print(auto(13))
# Дальше идет вторая часть задания, я не понял ее условие
for i in range(1, 10000000):
    if auto(i) > 97:
        print(i)
        break