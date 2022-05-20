"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    # def twoSum(self, nums: list[int], target: int) -> list[int]:
"""


class Solution_1:
    """ Solution 1
        O(n^2)
        5968ms, 15.1MB
        ind_1: for loop of nums
        ind_2: for loop of nums, ind_2 == target - ind_1
    """
    def twoSum(self, nums, target) -> list[int]:
        for ind_1 in range(len(nums)):
            for ind_2 in range(len(nums)):
                if nums[ind_1] + nums[ind_2] == target and ind_1 != ind_2:
                    return [ind_1, ind_2]


class Solution_2:
    """ Solution 2 (mine)
        O(n)
        372ms, 15.1MB
        ind_1: for loop of nums
        ind_2: the first element of nums[ind_1 + 1:] == target - nums[ind_1]
    """
    def twoSum(self, nums, target) -> list[int]:
        for ind_1 in range(len(nums)):
            diff = target - nums[ind_1]
            if diff in nums[ind_1 + 1:]:
                ind_2 = nums[ind_1 + 1:].index(diff) + ind_1 + 1
                return [ind_1, ind_2]


class Solution_3:
    """ Solution 3 (https://leetcode-cn.com/problems/two-sum/solution/xiao-bai-pythonji-chong-jie-fa-by-lao-la-rou-yue-j/) 
        O(n)
        44ms, 15.8MB
        ind_1: hash map of nums
        ind_2: search the hash map
    """
    def twoSum(self, nums, target) -> list[int]:
        hashmap = {}
        for ind_2, num_2 in enumerate(nums):
            hashmap[num_2] = ind_2
        for ind_1, num_1 in enumerate(nums):
            ind_2 = hashmap.get(target - num_1)
            if ind_2 is not None and ind_1 != ind_2:
                return [ind_1, ind_2]


# Test

sol = Solution_3()

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
nums = [2, 7, 11, 15]
target = 9
output1 = [0, 1]
output2 = [1, 0]
output_sol = sol.twoSum(nums, target)
print(True if output_sol == output1 or output_sol == output2 else False)

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
nums = [3,2,4]
target = 6
output1 = [1, 2]
output2 = [2, 1]
output_sol = sol.twoSum(nums, target)
print(True if output_sol == output1 or output_sol == output2 else False)

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
nums = [3, 3]
target = 6
output1 = [0, 1]
output2 = [1, 0]
output_sol = sol.twoSum(nums, target)
print(True if output_sol == output1 or output_sol == output2 else False)

import torch
torch.nn.GELU