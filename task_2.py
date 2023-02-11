'''
Напишите рекурсивную функцию, переводящую неотрицательное
целое число в двоичную систему. Воспринимайте 0 и 1 как базовые случаи с возвратом соответствующего строкового значения. Для остальных
положительных чисел n вам необходимо вычислить следующую цифру
при помощи оператора взятия остатка от деления и затем осуществить
рекурсивный вызов с вычислением цифр для n // 2. Наконец, вам нужно
сцепить строковый результат рекурсивного вызова со следующей циф-
152  Упражнения
рой, которую заранее надо преобразовать в строку, и вернуть полученную
строку в качестве результата функции.
Напишите основную программу, которая будет использовать рекурсивную функцию для преобразования неотрицательного числа, введенного
пользователем, из десятичной системы счисления в двоичную. Если будет
введено отрицательное значение, программа должна вывести соответствующее сообщение об ошибке.
'''
def task175(n):
    if n < 0:
        return 'Ошибка. Число меньше нуля.'
    if n < 2:
        return n
    b =''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

n = int(input())
print(task175(n))