# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# SOLUTION 1: Using two loops and if
# Time Complexity - O(n^3)

# def solution(nums: list, target: int):
#   res = [-1]
#   for i in nums:
#     for j in nums:
#       if i+j == target:
#         res.append(nums.index(i))
#   if len(res)>1:
#     res.remove(-1)
#   print(res)
#   if len(res)>1:
#     res.remove(-1)

# nums = [2,3,5,6] 
# target = 70

# solution(nums,target)

#===============================================================================#

# SOLUTION 2 : Using difference between element and target
# Time Complexity - O(n^2)

# def solution(nums: list, target: int):
#   diff = 0
#   num_in = [-1]
#   for i in nums:
#     diff = target - i
#     if diff in nums:
#       num_in.append(nums.index(i))
#   if len(num_in)>1:
#     num_in.remove(-1)
#   return num_in

# nums = [2,3,5,6] 
# target = 7

# result = solution(nums,target)
# print(result)

#===============================================================================#

# SOLUTION 3 : Using enumerate() as a hashmap
# Time Complexity - O(n) 

def solution(nums, target):
    seen = {}

    for index, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], index]

        seen[num] = index

    return [-1]

nums = [2, 3, 5, 6]
target = 7

result = solution(nums, target)
print(result)
