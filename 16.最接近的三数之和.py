#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (43.81%)
# Likes:    416
# Dislikes: 0
# Total Accepted:    98.1K
# Total Submissions: 223.2K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#


# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n_len = len(nums)
        dis_min = sum(nums[:3]) - target
        for cnt1 in range(n_len):
            if cnt1 > 0 and nums[cnt1] == nums[cnt1 - 1]:
                continue
            for cnt2 in range(cnt1 + 1, n_len):
                if cnt2 - 1 > cnt1 and nums[cnt2] == nums[cnt2 - 1]:
                    continue
                for cnt3 in range(cnt2 + 1, n_len):
                    if nums[cnt1] + nums[cnt2] + nums[cnt3] == target:
                        return target
                    elif abs(nums[cnt1] + nums[cnt2] + nums[cnt3] -
                             target) < abs(dis_min):
                        dis_min = nums[cnt1] + nums[cnt2] + nums[cnt3] - target
        return target + dis_min


# @lc code=end
