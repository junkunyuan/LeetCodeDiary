"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
    -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
"""

class Solution_1:
    """
    Solution 1: (my solution)
    O(N)
    time: 32ms; memory: 15MB
    """
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        stack = []
        while x:
            stack.append(x % 10)
            x = x // 10
        sum = 0
        times = 0
        while stack:
            sum += stack.pop(-1) * 10 ** times
            times += 1
        result = sign * sum
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0

        return result


class Solution_2:
    """
    Solution 2: (my solution)
    O(N)
    time: 36ms; memory: 14.9 MB
    """
    def reverse(self, x: int) -> int:
        y = 0
        if x == 0: return x
        pos_neg = -1 if x < 0 else 1
        x = abs(x)
        while x:
            y = y * 10
            y += (x % 10)
            x = x // 10

        if y < -2 ** 31 or y > 2 ** 31 - 1:
            return 0

        return (y * pos_neg)


class Solution_3:
    """
    Solution 3 (reference: https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/)
    """
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10

            if x < 0 and digit > 0:
                digit -= 10

            x = (x - digit) // 10
            rev = rev * 10 + digit
        
        return rev


# Test
# class Solution:
#     def reverse(self, x: int) -> int:


sol = Solution_2()

# Example 1:
# Input: x = 123
# Output: 321
input = 123
output = 321
output_sol = sol.reverse(input)
print(True if output_sol == output else False)

# Example 2:
# Input: x = -123
# Output: -321
input = -123
output = -321
output_sol = sol.reverse(input)
print(True if output_sol == output else False)

# Example 3:
# Input: x = 120
# Output: 21
input = 120
output = 21
output_sol = sol.reverse(input)
print(True if output_sol == output else False)

# Example 4:
# Input: x = 0
# Output: 0
input = 0
output = 0
output_sol = sol.reverse(input)
print(True if output_sol == output else False)
