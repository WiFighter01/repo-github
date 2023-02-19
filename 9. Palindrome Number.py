'''
Given an integer x, return true if x is a palindrome
, and false otherwise.
'''


def isPalindrome(x):
    str_x = str(x)
    if '-' in str(x):
        return False
    list_x = []
    for i in range(len(str_x)):
        list_x.append(x % 10)
        x = x // 10
    list_x_revers = list_x[::-1]
    if list_x == list_x_revers:
        return True
    else:
        return False
x = -1
print(isPalindrome(x))
