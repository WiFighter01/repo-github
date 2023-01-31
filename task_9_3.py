n, m = [int(i) for i in input().split()]
a = [['.'] * m for j in range(n)]

for i in range(n):
    if i % 2 == 0:
        for j in range(1, m , 2):
            a[i][j] = '*'
    elif i % 2 != 0:
        for j in range(0, m , 2):
            a[i][j] = '*'

for row in a:
    print(' '.join([str(elem) for elem in row]))
