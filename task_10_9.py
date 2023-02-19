'''
Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. Нужно определить сколько
языков знают все школьники, и сколько языков знает хотя бы один из школьников.

В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков, которое он
нает, а затем - названия языков, по одному в строке.

В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
 Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков. Языки нужно
  выводить в лексикографическом порядке, по одному на строке.
'''
n = int(input())

languages = []

for _ in range(n):
    k = int(input())
    buff = set()
    for _ in range(k):
        buff.add(input())
    languages.append(buff)

unic = set.union(*languages)
intersec = set.intersection(*languages)

print(len(intersec))
print('\n'.join(sorted(intersec)))
print(len(unic))
print('\n'.join(sorted(unic)))


# Решение разрабов:
# students = [{input() for j in range(int(input()))} for i in range(int(input()))]
# known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
# print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
# print(len(known_by_someone), *sorted(known_by_someone), sep='\n')