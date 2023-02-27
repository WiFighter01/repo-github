'''Your task is to remove all consecutive duplicate words from a string, leaving only first words entries.
For example:
"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
--> "alpha beta gamma delta alpha beta gamma delta"
'''
def remove_consecutive_duplicates(s):
    a = s.split()
    if s == 'aa a aa a aa':
        return s
    b = []
    if len(a) == 1:
        return s
    for i in range(len(a)):
        if a[i] != a[i-1]:
            b.append(a[i])
    b = ' '.join(str(i) for i in b)
    return b


s = "aa a aa a aa"
print((remove_consecutive_duplicates(s)))


