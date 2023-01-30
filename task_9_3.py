n, m = [int(i) for i in input().split()]
a = [[['.'] * n for i in range(n)] for j in range(m)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            a[i][j] = '*'
        else:
            a[i][j] = '*'

for row in a:
    print(' '.join([str(elem) for elem in row]))
