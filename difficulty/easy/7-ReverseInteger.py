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

"""

class Solution:
    """
    Solution 1: (my solution)
    O(N);
    time: 32ms; memory: 15MB;
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

class Solution:
    """
    Solution 2 (reference: https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/)
    """
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        rev = 0
        while x != 0:
            # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
            if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
                return 0
            digit = x % 10
            # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
            if x < 0 and digit > 0:
                digit -= 10

            # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
            x = (x - digit) // 10
            rev = rev * 10 + digit
        
        return rev


sol = Solution
inp = [123, -123, 120, 0]
out = [321, -321, 21, 0]
for i in range(len(inp)):
    answer = sol.reverse(None, inp[i])
    print(inp[i], out[i], answer)
