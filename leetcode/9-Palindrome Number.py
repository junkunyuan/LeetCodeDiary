"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:
    -231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
"""


class Solution_1:
    """
    Solution 1:
    O(logN), O(logN)
    92ms, 15MB
    """
    def isPalindrome(self, x: int) -> bool:
        l = []
        # if x is negative, false
        if x < 0:
            return False
        else:
            while x:
                s = x % 10
                l.append(s)
                x = x // 10
            half = len(l) // 2
            if half == 0: return True
            for i in range(half):
                if l[i] != l[-1-i]:
                    return False
            return True


class Solution_2:
    """
    Solution 2: (https://leetcode.cn/problems/palindrome-number/solution/hui-wen-shu-by-leetcode-solution/)
    O(logN), O(1)
    60ms, 14.8MB
    """
    def isPalindrome(self, x: int) -> bool:
        l = []
        # if x is negative or is 10x, false
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverterd_number = 0
        while x > reverterd_number:
            reverterd_number = reverterd_number * 10 + x % 10
            x = x // 10
        return (x == reverterd_number) or (x == reverterd_number // 10)


# Test
sol = Solution_2()

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
input = 121
output = True
output_sol = sol.isPalindrome(input)
print(True if output_sol == output else False)


# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
input = -121
output = False
output_sol = sol.isPalindrome(input)
print(True if output_sol == output else False)

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
input = 10
output = False
output_sol = sol.isPalindrome(input)
print(True if output_sol == output else False)