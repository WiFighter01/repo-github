def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    # место для Вашего кода
    if n % 10 == 1:
        return f'{n} процент'




for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
