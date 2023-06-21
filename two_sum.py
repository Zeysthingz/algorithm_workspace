
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

import sys
import random

class Sum_Two:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def two_sum(self):
        num_dict = {}
        for i,num in enumerate(self.nums):
            val= self.target - num
            if val in num_dict:
                return print([num_dict[val], i])
            num_dict[num] = i
        return []


# Parse the command-line arguments
nums = [int(arg) for arg in sys.argv[1:-1]]
target = int(sys.argv[-1])

result = Sum_Two(nums, target)
result.two_sum()