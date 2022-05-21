"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Constraints:
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
"""
             

class Solution_1:
    def isValid(self, s: str) -> bool:
        s = list(s)
        stack = []
        mapping = {'(': 1, ')': -1, '[': 2, ']': -2, '{': 3, '}': -3}
        while s:
            # From left to right (pop(0)) and from right to left (pop) are both OK
            curr = s.pop(0)
            if len(stack) !=0:
                if mapping[stack[-1]] + mapping[curr] != 0:
                    # If begin with ), ], or }, return False
                    if mapping[curr] < 0:
                        return False
                    stack.append(curr)
                else:
                    stack.pop()
            else:
                if mapping[curr] < 0:
                        return False
                stack.append(curr)
        return True if len(stack) == 0 else False
            
class Solution_2:
    """
    Solution 2
    https://leetcode.cn/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
    O(n), O(n+|char set|)
    """
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack


# Test
sol = Solution_2()

# Example 1:
# Input: s = "()"
# Output: true
input = "(){}}{"
output = False
output_sol = sol.isValid(input)
print(True if output_sol == output else False)

# Example 2:
# Input: s = "()[]{}"
# Output: true
input = "()[]{}"
output = True
output_sol = sol.isValid(input)
print(True if output_sol == output else False)

# Example 3:
# Input: s = "(]"
# Output: false
input = "(]"
output = False
output_sol = sol.isValid(input)
print(True if output_sol == output else False)
