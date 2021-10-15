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

Example 4:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

class Solution:
    """ Solution 1 (https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/)
    O(n);
    time: ms; memory: MB; 
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


class Solution2:
    """ resolve
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_cur = set()
        right, max_len = 0, 0
        n = len(s)
        for i in range(n):
            if i > 0 and s[i - 1] in str_cur:
                str_cur.remove(s[i - 1])
            while right <= n - 1 and s[right] not in str_cur:
                str_cur.add(s[right])
                right += 1
            max_len = max(max_len, right - i)
        return max_len

sol = Solution2
s = ["abcabcbb", "bbbbb", "pwwkew", "a"]
answer = [3, 1, 3, 0]
for i in range(len(answer)):
    len_max = sol.lengthOfLongestSubstring(None, s[i])
    print(answer[i], len_max)
