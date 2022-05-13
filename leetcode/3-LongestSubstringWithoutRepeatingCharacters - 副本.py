"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:=
Input: s = ""
Output: 0

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
"""

class Solution_1:
    """ Solution 1 (https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/)
    O(n);
    time: 68ms; memory: 15.1 MB 
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Construct hash set
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # Move left pointer
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # Move right pointer
                occ.add(s[rk + 1])
                rk += 1
            # Check the max length string
            ans = max(ans, rk - i + 1)
        return ans



# Test
sol = Solution_1()

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
input = "abcabcbb"
output = 3
output_sol = sol.lengthOfLongestSubstring(input)
print(output_sol)
print(True if output_sol == output else False)

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
input = "bbbbb"
output = 1
output_sol = sol.lengthOfLongestSubstring(input)

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
input = "pwwkew"
output = 3
output_sol = sol.lengthOfLongestSubstring(input)
print(True if output_sol == output else False)

# Example 4:=
# Input: s = ""
# Output: 0
input = ""
output = 0
output_sol = sol.lengthOfLongestSubstring(input)
print(True if output_sol == output else False)
