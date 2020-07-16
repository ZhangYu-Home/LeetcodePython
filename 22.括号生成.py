#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.31%)
# Likes:    1010
# Dislikes: 0
# Total Accepted:    124.7K
# Total Submissions: 165.5K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#

# @lc code=start
class Solution:
    #def generateParenthesis(self, n: int) -> List[str]:
    def generateParenthesis(self, n):
        cur_str = [" "]*2*n
        l_s = []
        self.generateAll(cur_str, 0, l_s)
        return l_s

    def generateAll(self, cur_str, pos, l_s):
        print(cur_str)
        if pos == len(cur_str):
            if(self.validStr(cur_str)):
                l_s.append("".join(cur_str))
        else:
            cur_str[pos] = '('
            self.generateAll(cur_str, pos+1, l_s)
            cur_str[pos] = ')'
            self.generateAll(cur_str, pos+1, l_s)

    def validStr(self, cur_str):
        balance = 0
        for i in cur_str:
            if i == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

if __name__ == "__main__":
    print(Solution().generateParenthesis(3))

        
# @lc code=end

