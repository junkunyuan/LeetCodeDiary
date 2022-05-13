"""
912. Sort an Array

Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
"""

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick_sort(nums: list[int], l: int, r: int) -> int:
            if l >= r:
                return
            index = random.randint(l, r)
            pivot = nums[index]
            nums[l], nums[index] = nums[index], nums[l]
    
            begin, end = l, r
            while l < r:
                while l < r and nums[r] >= pivot:
                    r -= 1
                while l < r and nums[l] <= pivot:
                    l += 1
                if l != r:
                    nums[l], nums[r] = nums[r], nums[l]
            nums[begin], nums[l] = nums[l], nums[begin]
            quick_sort(nums, begin, l - 1)
            quick_sort(nums, l + 1, end)

        quick_sort(nums, 0, len(nums) - 1)
        return nums

    
