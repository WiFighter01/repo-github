def second_symbol(s, symbol):
    a = s.find(symbol)
    first_part = s[:a+1]
    second_part = s[a+1:]
    res = len(first_part) + second_part.find(symbol)
    if s.count(symbol) < 2:
        return -1
    else:
        return res

s = 'Hello world!!!'
symbol = 'o'

print(second_symbol(s, symbol))