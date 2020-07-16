#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (37.03%)
# Likes:    987
# Dislikes: 0
# Total Accepted:    241.9K
# Total Submissions: 651.5K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l_len = len(strs)  #字符串数组长度
        if l_len == 0:
            return ''
        s_len_min = min([len(s) for s in strs])
        s_pre = ''
        for i in range(s_len_min):
            for j in range(l_len):
                if strs[j][i] != strs[0][i]:
                    return s_pre
            s_pre += strs[0][i]
        return s_pre


# @lc code=end
