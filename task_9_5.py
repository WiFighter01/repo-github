n = int(input())
a = [[0] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            a[i][j] = 1
    for j in range(n - 1 - i):
        a[i][j] = 0
    for j in range(n - i, n):
        a[i][j] = 2

for row in a:
    print(' '.join([str(elem) for elem in row]))
