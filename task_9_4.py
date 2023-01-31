n = int(input())
a = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][i] = 0
        for j in range(i + 1, n):
            a[i][j] = i + 1
        for j in range(0, i):
            a[i][j] = i





for row in a:
    print(' '.join([str(elem) for elem in row]))