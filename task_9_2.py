n = int(input())
a = [['.'] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = '*'
        elif i == int(n / 2):
            a[i][j] = '*'
        elif j == int(n / 2):
            a[i][j] = '*'
        elif i + j == n - 1:
            a[i][j] = '*'
for row in a:
    print(' '.join([str(elem) for elem in row]))

