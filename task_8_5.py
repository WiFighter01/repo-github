def revers_numb(x):
    list_numbers = []
    while list_numbers != 0:
        list_numbers.append(int(input()))
    res = list_numbers.reverse()
    return res

x = int(input())
print(revers_numb(x))
