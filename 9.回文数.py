#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (57.43%)
# Likes:    1019
# Dislikes: 0
# Total Accepted:    314.9K
# Total Submissions: 548.1K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #负数和末位为0的非零数字均不是回文数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + (x % 10)
            x = x // 10
        return x == y or x == y // 10


# @lc code=end
