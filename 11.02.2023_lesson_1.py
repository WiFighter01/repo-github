'''
Множества
'''

import sys
import timeit


def auto(N):
    # int(bin(N)[2:].replace('0', ''), 2) запись в одну строку
    res = bin(N)[2:] #1
    res = res.replace('0', '') #2
    res = int(res, 2) #3
    return res

# Решение через список (долгое):
a = []
for n in range(100, 1001):
    r = auto(n)
    if not r in a:
        a.append(r)

print(a, len(a))


# Решение через множество (быстрое):
a = set()
for n in range(100, 1001):
    r = auto(n)
    a.add(r)
print(a, len(a))
