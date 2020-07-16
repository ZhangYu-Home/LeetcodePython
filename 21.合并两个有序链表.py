#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (61.30%)
# Likes:    1028
# Dislikes: 0
# Total Accepted:    259.9K
# Total Submissions: 417.4K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #递归写法
        if not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


        #非递归写法
        # if not l1:
        #     return l2
        # elif not l2:
        #     return l1
        # #保证l1的第一个小于l2的第一个：
        # if l1.val > l2.val:
        #     return self.mergeTwoLists(l2, l1)

        # lr = l1
        # lt1 = l1.next
        # while lt1:
        #     if lt1.val <= l2.val:
        #         l1 = l1.next
        #         lt1 = lt1.next
        #     else:
        #         l1.next = l2
        #         #因为上边的判断语句已经进行了一次比较，所以此处继续后移一次
        #         l1 = l1.next
        #         l2 = lt1
        #         lt1 = l1.next
        # l1.next = l2
        # return lr

# @lc code=end
