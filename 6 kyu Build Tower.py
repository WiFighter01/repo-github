def tower_builder(n_floors):
    a = [[' ' for i in range(n_floors * 2 - 1)] for j in range(n_floors)]
    a[0][n_floors - 1] = '*'
    for i in range(n_floors):
        for j in range(n_floors * 2 - 1):
            if a[i-1][j] == '*':
                a[i][j-1], a[i][j], a[i][j+1] = '*', '*', '*'
    for i in range(n_floors):
        for j in range(n_floors * 2 - 1):
            print(*a)


n_floors = 5
print(tower_builder(n_floors))