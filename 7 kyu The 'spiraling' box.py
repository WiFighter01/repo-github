def create_box(m, n):  ## m and n positive integers
    a = [[0] * m for i in range(n)]
    z = 1
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1:
                a[i][j] = z
            if j == 0 or j == m - 1:
                a[i][j] = z

    return a

m = 5
n = 8
print(create_box(m, n))