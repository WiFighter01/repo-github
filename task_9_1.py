n, m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
res_1, res_2 = 0, 0
curr_max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            res_1, res_2 = i, j
print(res_1, res_2)

