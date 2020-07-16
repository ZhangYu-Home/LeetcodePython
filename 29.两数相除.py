#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (19.79%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    50.7K
# Total Submissions: 255.3K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
# 
# 返回被除数 dividend 除以除数 divisor 得到的商。
# 
# 整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) =
# -2
# 
# 
# 
# 示例 1:
# 
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
# 
# 示例 2:
# 
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 解释: 7/-3 = truncate(-2.33333..) = -2
# 
# 
# 
# 提示：
# 
# 
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
# 
# 
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #排除唯一超范围的情形
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        result = 0
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        # 左移的位数
        mov_cnt = -1
        while abs_dividend >= (abs_divisor << (mov_cnt+1)):
            mov_cnt += 1
        # 利用移位运算加快速度
        while mov_cnt > -1:
            if abs_dividend >= (abs_divisor << mov_cnt):
                abs_dividend = abs_dividend - (abs_divisor << mov_cnt)
                result += (1 << mov_cnt)
            mov_cnt -= 1

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return 0 - result    

        return result
# @lc code=end

