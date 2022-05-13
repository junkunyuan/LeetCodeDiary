"""
4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
"""

class Solution:
    """
    Solution 1 (reference: https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/)
    """
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def getKthElement(k):
            """
            Binary search
            """
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    # find the new "k-th"
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    # find the new "k-th"
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


# Test
sol = Solution()

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
input1 = [1, 3]
input2 = [2]
output = 2.0
output_sol = sol.findMedianSortedArrays(input1, input2)
print(True if output_sol == output else False)

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
input1 = [1, 2]
input2 = [3, 4]
output = 2.5
output_sol = sol.findMedianSortedArrays(input1, input2)
print(True if output_sol == output else False)

# Example 3:
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
input1 = [0, 0]
input2 = [0, 0]
output = 0.0
output_sol = sol.findMedianSortedArrays(input1, input2)
print(True if output_sol == output else False)

# Example 4:
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
input1 = []
input2 = [1]
output = 1.0
output_sol = sol.findMedianSortedArrays(input1, input2)
print(True if output_sol == output else False)

# Example 5:
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
input1 = [2]
input2 = []
output = 2.0
output_sol = sol.findMedianSortedArrays(input1, input2)
print(True if output_sol == output else False)
