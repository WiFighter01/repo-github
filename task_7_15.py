n, k = [int(i) for i in input().split()]
a = ['I' for i in range(n)]

for i in range(k):
    l1, r1 = [int(i) for i in input().split()]
    for j in range(l1 -1, r1):
        a[j] = '.'

print(''.join([str(i) for i in a]))
