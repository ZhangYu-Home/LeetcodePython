#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (53.24%)
# Likes:    696
# Dislikes: 0
# Total Accepted:    109.3K
# Total Submissions: 204.8K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if "" == digits:
            return []
        
        dict_dig2char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        #过滤所有不属于2-9的字符，转化为了列表
        # digits = list(filter(lambda x: x in dict_dig2char.keys(), digits))
        # l_res = list(dict_dig2char[digits[0]])
        # for c_i in digits[1:]:
        #     l_res = [s1+s2 for s1 in l_res for s2 in list(dict_dig2char[c_i])]
        # return l_res
        
        #下边是直接使用迭代器完成的
        digits = filter(lambda x: x in dict_dig2char.keys(), digits)
        l_res = list(dict_dig2char[next(digits)])
        for c_i in digits:
            l_res = [s1+s2 for s1 in l_res for s2 in list(dict_dig2char[c_i])]
        return l_res

                


# @lc code=end
