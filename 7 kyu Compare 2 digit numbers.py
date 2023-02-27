def compare(a, b):
    nums = []
    for i in range(2):
        aa = a % 10
        nums.append(aa)
        a = a // 10
    for i in range(2):
        bb = b % 10
        nums.append(bb)
        b = b // 10
    nums = nums[::-1]
    if nums[0] == nums[2] and nums[1] == nums[3]:
        return '100%'
    elif nums[0] == nums[3] and nums[1] == nums[2]:
        return '100%'
    elif nums[0] == nums[2] and nums[1] != nums[3]:
        return '50%'
    elif nums[0] == nums[3] and nums[1] != nums[2]:
        return '50%'
    elif (nums[0] != nums[2] and nums[1] != nums[3]) and (nums[0] != nums[3] and nums[1] != nums[2]):
        return '0%'
    elif nums[0] != nums[2] and nums[1] == nums[3]:
        return '50%'
    elif nums[0] != nums[3] and nums[1] == nums[2]:
        return '50%'


a = 14
b = 24
print(compare(a, b))