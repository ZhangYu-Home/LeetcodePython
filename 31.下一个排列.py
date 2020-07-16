#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (33.74%)
# Likes:    526
# Dislikes: 0
# Total Accepted:    67.3K
# Total Submissions: 199K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        if lens < 2:
            return
        
        for i in range(lens-1,0,-1):
            if nums[i] > nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
                p_f = i + 1
                p_b = lens-1
                while p_f < p_b:
                    nums[p_f],nums[p_b] = nums[p_b],nums[p_f]
                    p_f += 1
                    p_b -= 1
                p_f = i
                for j in range(i+1,lens):
                    if nums[p_f] > nums[j]:
                        nums[p_f], nums[j] = nums[j], nums[p_f]
                        p_f += 1
                return
        p_f = 0
        p_b = lens-1
        while p_f < p_b:
            nums[p_f],nums[p_b] = nums[p_b],nums[p_f]
            p_f += 1
            p_b -= 1

        




# @lc code=end

