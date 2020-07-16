#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.17%)
# Likes:    765
# Dislikes: 0
# Total Accepted:    146.9K
# Total Submissions: 192.5K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permute(self, nums):
        lens = len(nums)
        if 0 == lens:
            return []
        if 1 == lens:
            return [nums]
        
        sub_permute = self.permute(nums[1:])
        l_res = []
        for l_tmp in sub_permute:
            for cnt_pos in range(lens):
                l_tmp1 = l_tmp.copy()
                l_tmp1.insert(cnt_pos,nums[0])
                l_res.append(l_tmp1)

        return l_res
    

# @lc code=end

