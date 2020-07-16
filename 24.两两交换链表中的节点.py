#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (65.76%)
# Likes:    520
# Dislikes: 0
# Total Accepted:    113.6K
# Total Submissions: 172.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        #临时头结点
        p_head = ListNode(0)
        p_head.next = head
        p_front = p_head
        p_tail = head
        while True:
            p_front.next = p_tail.next
            p_tail.next = p_tail.next.next
            p_front.next.next = p_tail
            #切换位置
            p_front = p_tail
            p_tail = p_tail.next
            if p_tail is None or p_tail.next is None:
                break
                   
        return p_head.next
# @lc code=end
