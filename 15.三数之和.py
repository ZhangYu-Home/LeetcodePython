#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (26.66%)
# Likes:    2069
# Dislikes: 0
# Total Accepted:    211.3K
# Total Submissions: 788.6K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # res = []
        # if (n < 3):
        #     return []
        # nums.sort()
        # res = []
        # for i in range(n):
        #     if (nums[i] > 0):
        #         return res
        #     if (i > 0 and nums[i] == nums[i - 1]):
        #         continue
        #     L = i + 1
        #     R = n - 1
        #     while (L < R):
        #         if (nums[i] + nums[L] + nums[R] == 0):
        #             res.append([nums[i], nums[L], nums[R]])
        #             while (L < R and nums[L] == nums[L + 1]):
        #                 L = L + 1
        #             while (L < R and nums[R] == nums[R - 1]):
        #                 R = R - 1
        #             L = L + 1
        #             R = R - 1
        #         elif (nums[i] + nums[L] + nums[R] > 0):
        #             R = R - 1
        #         else:
        #             L = L + 1
        # return res

        nums.sort()
        len_s = len(nums)
        if len_s < 3:
            return []
        result = []
        for cnt1 in range(len_s):
            if cnt1 > 0 and nums[cnt1] == nums[cnt1 - 1]:
                continue
            if nums[cnt1] > 0:
                break
            for cnt2 in range(cnt1 + 1, len_s):
                if cnt2 - 1 > cnt1 and nums[cnt2] == nums[cnt2 - 1]:
                    continue
                if nums[cnt1] + nums[cnt2] + nums[cnt2] > 0:
                    break
                for cnt3 in range(cnt2 + 1, len_s):
                    if cnt3 - 1 > cnt2 and nums[cnt3] == nums[cnt3 - 1]:
                        continue
                    if nums[cnt1] + nums[cnt2] + nums[
                            cnt3] == 0:  # and r_t not in result:
                        result.append([nums[cnt1], nums[cnt2], nums[cnt3]])
                        break
        return result


# @lc code=end
