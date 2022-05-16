"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
    1 <= n <= 45

class Solution:
    def climbStairs(self, n: int) -> int:
"""

class Solution_1:
    """
    solution 1
    O(n); O(n)
    32ms; 14.8MB
    """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         x, y = 1, 1
#         for _ in range(1, n):
#             x, y = y, x + y
#         return y

# Test
sol = Solution()

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
input = 2
output = 2
output_sol = sol.climbStairs(input)
print(True if output_sol == output else False)

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
input = 5
output = 8
output_sol = sol.climbStairs(input)
print(True if output_sol == output else False)