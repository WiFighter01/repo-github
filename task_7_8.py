a = [int(i) for i in input().split()]
elements = 1
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        elements += 1
print(elements)
