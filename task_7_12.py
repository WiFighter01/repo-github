a = [int(i) for i in input().split()]
kc = [int(i) for i in input().split()]
k = kc[0]
c = kc[1]
a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = c
print(' '.join([str(i) for i in a]))
