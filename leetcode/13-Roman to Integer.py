"""
13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution:
    def romanToInt(self, s: str) -> int:
"""


class Solution_1:
    """
    Solutin 1 (mine)
    O(n); O(1)
    68ms; 15.1MB
    """
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = len(s)
        d = 0  # digit
        i = 0  # search index
        while (i != l):
            t1 = dic[s[i]]
            if i < l - 1:
                t2 = dic[s[i + 1]]
                if t2 > t1:
                    t1 = t2 - t1
                    i += 1
            d += t1
            i += 1 
        return d

class Solution_2:
    """
    Solutin 2 (https://leetcode.cn/problems/roman-to-integer/solution/luo-ma-shu-zi-zhuan-zheng-shu-by-leetcod-w55p/)
    O(n); O(1)
    36ms; 15MB
    """
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        l = len(s)
        d = 0
        for i in range(l):
            t1 = dic[s[i]]
            if (i < l - 1) and (t1 <  dic[s[i + 1]]):
                d -= t1
            else:
                d += t1
        return d

# Test
sol = Solution_2()

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
input = "III"
output = 3
output_sol = sol.romanToInt(input)
print(True if output_sol == output else False)

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
input = "LVIII"
output = 58
output_sol = sol.romanToInt(input)
print(True if output_sol == output else False)

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
input = "MCMXCIV"
output = 1994
output_sol = sol.romanToInt(input)
print(True if output_sol == output else False)
