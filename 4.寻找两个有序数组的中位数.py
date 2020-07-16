#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (37.33%)
# Likes:    2488
# Dislikes: 0
# Total Accepted:    179.8K
# Total Submissions: 481.5K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m > n:
            #保证nums1长度小于等于nums2
            return self.findMedianSortedArrays(nums2, nums1)
        #此时可保证m<=n
        iMin = 0
        iMax = m
        while iMin <= iMax:
            i = (iMax + iMin) // 2
            j = (m + n + 1) // 2 - i
            if j != 0 and i != m and nums2[j - 1] > nums1[i]:
                iMin = i + 1
            elif i != 0 and j != n and nums1[i - 1] > nums2[j]:
                iMax = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:
                    return maxLeft  # 奇数的话不需要考虑右半部分

                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums2[j], nums1[i])

                return (maxLeft + minRight) / 2  #如果是偶数的话返回结果

        return 0.0


# @lc code=end
