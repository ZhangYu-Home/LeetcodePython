#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (38.42%)
# Likes:    809
# Dislikes: 0
# Total Accepted:    165.2K
# Total Submissions: 428.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        n1_t = head
        for cnt1 in range(n - 1):
            n1_t = n1_t.next
        if not n1_t.next:
            return head.next
        n1_t = n1_t.next
        n2_t = head
        while n1_t.next:
            n1_t = n1_t.next
            n2_t = n2_t.next
        n2_t.next = n2_t.next.next
        return head


# @lc code=end
