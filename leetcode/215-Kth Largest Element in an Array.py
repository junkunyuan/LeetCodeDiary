"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        while True:
            idx = self.partition(nums, l, r)
            if idx == k - 1:
                return nums[idx]
            elif idx < k - 1:
                l = idx + 1
            else:
                r = idx - 1

    # quick sort
    def partition(self, nums: list[int], l: int, r: int) -> int:
        pivot = nums[l]
        begin = l
        while l < r:
            while l < r and nums[r] <= pivot:
                r -= 1
            while l < r and nums[l] >= pivot:
                l += 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[begin], nums[l] = nums[l], nums[begin]
        return l

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        while True:
            idx = self.quick_sort(nums, l, r)
            if idx == k - 1:
                return nums[idx]
            elif idx < k - 1:
                l = idx + 1
            else:
                r = idx - 1

    def quick_sort(self, nums: list[int], l:int, r: int) -> int:
        pivot = nums[l]
        begin = l
        while l < r:
            while (l < r) and (nums[r] <= pivot):
                r -= 1
            while (l < r) and (nums[l] >= pivot): 
                l += 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[begin], nums[l] = nums[l], nums[begin]
        return l




# Test
sol = Solution()

# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
input = [3,2,1,5,6,4]
k = 2
output = 5
output_sol = sol.findKthLargest(input, k)
print(True if output_sol == output else False)

# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
input = [3,2,3,1,2,4,5,5,6]
k = 4
output = 4
output_sol = sol.findKthLargest(input, k)
print(True if output_sol == output else False)
