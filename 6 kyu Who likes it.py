def likes(names):
    if len(names) == 0:
        res = 'no one likes this'
        return res
    elif len(names) == 1:
        res = f'{names[0]} likes this'
        return res
    elif len(names) == 2:
        res = f'{names[0]} and {names[1]} like this'
        return res
    elif len(names) == 3:
        res = f'{names[0]}, {names[1]} and {names[2]} like this'
        return res
    elif len(names) > 3:
        res = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
        return res


names = ["Alex", "Jacob", "Mark", "Max", '', '']
print(likes(names))