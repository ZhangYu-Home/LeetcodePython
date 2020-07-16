#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (48.65%)
# Likes:    8385
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 
# 
# 
# 示例:
# 
# 给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        第一种解法：436ms
        len_nums = len(nums)
        for i in range(1, len_nums):
            if target-nums[i] in nums[:i]:
                return i,nums[:i].index(target-nums[i])
        return []
        """
        #第二种解法，使用哈希表，即字典：用时仅64ms
        #这种思路处理查找方法外，思路与上边的相同
        hashmap = {}
        for ind, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [ind, hashmap.get(target - num)]
            hashmap[num] = ind
        
# @lc code=end

