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
    def sortArray(self, nums: list[int]) -> list[int]:
"""


class Solution_1:
    """
    Solution 1
    Quick sort
    428ms, 20.7MB
    O(NlogN), O(h)  (h: recursion levels)
    """
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick_sort(nums: list[int], l: int, r: int) -> int:
            if l >= r:
                return
            import random
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


class Solution_2:
    """
    Solution 2
    Heat sort
    760ms, 21.2MB
    O(NlogN), O(1)
    """
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break
        
    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)
            
    def sortArray(self, nums: list[int]) -> list[int]:
        self.heap_sort(nums)
        return nums


class Solution_3:
    """
    Solution 3
    Merge sort
    O(NlogN), O(N)
    508ms, 20.9MB
    """
    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp

    def sortArray(self, nums: list[int]) -> list[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums


# Test
sol = Solution_1()

# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
input = [5,2,3,1]
output = [1,2,3,5]
output_sol = sol.sortArray(input)
print(True if output_sol == output else False)

# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
input = [5,1,1,2,0,0]
output = [0,0,1,1,2,5]
output_sol = sol.sortArray(input)
print(True if output_sol == output else False)









    
