a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]
# for i in a:
#     for j in i:
#         print(j, end=' ')
#     print()
# обход по индексам:

for i in range(3):
    for j in range(4):
        print(a[i][j], end=' ')
    print()
