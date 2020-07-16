#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.87%)
# Likes:    3527
# Dislikes: 0
# Total Accepted:    450.1K
# Total Submissions: 1.3M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = ""
        len_s1 = 0
        ind = 0
        while ind < len(s):
            if s[ind] in s1:
                len_s1 = max(len_s1,len(s1))
                s1 = s1[s1.index(s[ind])+1:]+s[ind]
            else:
                s1 += s[ind]
            ind+=1
        len_s1 = max(len_s1,len(s1)) #防止整个字符串完全不同的情形。
        return len_s1
# @lc code=end

