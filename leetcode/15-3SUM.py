"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # Enumerate a
        for first in range(n):
            # Be different from the previous one
            if nums[first] == nums[first - 1] and first > 0:
                continue
            third = n - 1
            target = -nums[first]
            # Enumerate b
            for second in range(first + 1, n):
                # Be different from the previous one
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


# Test
sol = Solution()

# Example test:
# Input: nums = [0, 0, 0]
# Output: [0, 0, 0]
input =  [0, 0, 0]
output =  [ [0, 0, 0]]
output_sol = sol.threeSum(input)
print(True if output_sol == output else False)

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
input = [-1,0,1,2,-1,-4]
output =  [[-1,-1,2],[-1,0,1]]
output_sol = sol.threeSum(input)
print(True if output_sol == output else False)

# Example 2:
# Input: nums = []
# Output: []
input = []
output = []
output_sol = sol.threeSum(input)
print(True if output_sol == output else False)

# Example 3:
# Input: nums = [0]
# Output: []
input = [0]
output = []
output_sol = sol.threeSum(input)
print(True if output_sol == output else False)
