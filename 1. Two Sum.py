'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


def twoSum(nums, target):
    output_list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            if nums[i] + nums[j] == target:
                output_list.append(i)
                output_list.append(j)
                return output_list


nums = [3, 2, 2, 3]
target = 6
print(twoSum(nums, target))
