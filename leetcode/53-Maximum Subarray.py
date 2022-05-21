"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
"""


class Solution_1:
    """
    Solution 1:
    96ms, 25.5MB
    """
    def maxSubArray(self, nums: list[int]) -> int:
        max_num = nums[0]
        # Current sum value (no subarray is 0)
        curr = 0
        for _, num in enumerate(nums):
            if num < 0:
                if curr == 0:
                    # If there is another negative value greater than the first negative value
                    if num > max_num:
                        max_num = num
                    # We want a non-negative when curr is 0 (no subarray)
                    continue
                else:
                    # If the cumulative current sum is smaller, then empty subarray
                    if num + curr < 0:
                        curr = 0
                    else:
                        curr += num
            else:
                curr += num
            if curr > max_num:
                max_num = curr
        return max_num


class Solution_2:
    """
    Solution 2
    https://leetcode.cn/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/
    144ms, 25.9MB
    """
    def maxSubArray(self, nums: list[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)



# Test
sol = Solution_2()

# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = 6
output_sol = sol.maxSubArray(input)
print(True if output_sol == output else False)

# Example 2:
# Input: nums = [1]
# Output: 1
input = [1]
output = 1
output_sol = sol.maxSubArray(input)
print(True if output_sol == output else False)

# Example 3:
# Input: nums = [5, 4, -1, 7, 8]
# Output: 23
input = [5, 4, -1, 7, 8]
output = 23
output_sol = sol.maxSubArray(input)
print(True if output_sol == output else False)
