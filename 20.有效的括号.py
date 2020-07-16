#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (41.45%)
# Likes:    1554
# Dislikes: 0
# Total Accepted:    272.1K
# Total Submissions: 655.3K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
#
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
#
#
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
#
#
# 示例 3:
#
# 输入: "(]"
# 输出: false
#
#
# 示例 4:
#
# 输入: "([)]"
# 输出: false
#
#
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
#
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {'(': ')', '[': ']', '{': '}'}
        l_s = []
        ind_st = 0
        len_s = len(s)
        while ind_st < len_s:
            if l_s != []:
                if dict1[l_s[-1]] == s[ind_st]:
                    l_s.pop()
                    ind_st += 1
                elif s[ind_st] in dict1.keys():
                    l_s.append(s[ind_st])
                    ind_st += 1
                else:
                    break
            else:
                if s[ind_st] in dict1.keys():
                    l_s.append(s[ind_st])
                    ind_st += 1
                else:
                    break

        return ind_st == len_s and l_s == []

# @lc code=end
