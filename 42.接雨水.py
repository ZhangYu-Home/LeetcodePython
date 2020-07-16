#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (50.77%)
# Likes:    1254
# Dislikes: 0
# Total Accepted:    97K
# Total Submissions: 190.7K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        len_h = len(height)
        rain_h = 0
        iMin = 0
        iMax = len_h - 1
        while iMin < iMax:
            if height[iMin] < height[iMax]:
                rec_t = height[iMin]
                iMin += 1
                while rec_t > height[iMin]:
                    rain_h += (rec_t - height[iMin])
                    iMin += 1
            else:
                rec_t = height[iMax]
                iMax -= 1
                while rec_t > height[iMax]:
                    rain_h += (rec_t - height[iMax])
                    iMax -= 1
        return rain_h


# @lc code=end
