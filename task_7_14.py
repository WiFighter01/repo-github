a = [int(i) for i in input().split()]
final_list = []
for elem in range(len(a)):
    if a.count(a[elem]) == 1:
        final_list.append(a[elem])
print(' '.join([str(i) for i in final_list]))

