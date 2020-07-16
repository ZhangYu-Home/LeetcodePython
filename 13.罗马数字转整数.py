#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (61.34%)
# Likes:    880
# Dislikes: 0
# Total Accepted:    189.6K
# Total Submissions: 308.6K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
#
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: "III"
# 输出: 3
#
# 示例 2:
#
# 输入: "IV"
# 输出: 4
#
# 示例 3:
#
# 输入: "IX"
# 输出: 9
#
# 示例 4:
#
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
#
#
# 示例 5:
#
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        #第一种：
        rom_l = [
            'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV',
            'I'
        ]
        div_l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ind = 0
        num = 0
        while len(s) > 1:
            if s[0] == rom_l[ind]:
                num += div_l[ind]
                s = s[1:]
            elif s[:2] == rom_l[ind]:
                num += div_l[ind]
                s = s[2:]
            else:
                ind += 1
        if len(s) == 1:
            num += div_l[rom_l.index(s)]
        return num

        #第二种：
        # rom_l = [
        #     'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV',
        #     'I'
        # ]
        # div_l = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        # ind = 0
        # num = 0
        # while True:
        #     if len(s) and s[0] == rom_l[ind]:
        #         num += div_l[ind]
        #         s = s[1:]
        #     elif len(s) > 1 and s[:2] == rom_l[ind]:
        #         num += div_l[ind]
        #         s = s[2:]
        #     elif len(s) == 0:
        #         break
        #     else:
        #         ind += 1
        # return num

        #第三种：
        # d = {
        #     'I': 1,
        #     'IV': 3,
        #     'V': 5,
        #     'IX': 8,
        #     'X': 10,
        #     'XL': 30,
        #     'L': 50,
        #     'XC': 80,
        #     'C': 100,
        #     'CD': 300,
        #     'D': 500,
        #     'CM': 800,
        #     'M': 1000
        # }
        # #这种写法是真的巧！！！
        # return sum(
        #     d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))


# @lc code=end
