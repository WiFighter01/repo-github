a = [int(i) for i in input().split()]
mmin = 100000000000000
mmax = 0
for i in a:
    if i > mmax:
        mmax = i
    if i < mmin:
        mmin = i
a_final = []
for i in range(len(a)):
    if a[i] == mmax:
        a[i] = mmin
    elif a[i] == mmin:
        a[i] = mmax
    a_final.append(a[i])
print(' '.join([str(i) for i in a_final]))