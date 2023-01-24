def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""

    if n == 11 or n == 12 or n ==13 or n == 14:
        return f'{n} процентов'
    elif n % 10 == 1:
        return f'{n} процент'
    elif n % 10 == 2 or n % 10 == 3 or n % 10 ==4:
        return f'{n} процента'
    else:
        return f'{n} процентов'


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
