'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums) - 1):
        if nums[i] + nums[i+1] == target:
             return list(a[i], a[i+1])

nums = []
while
target = int(input())
print(twoSum(nums, target))