#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (61.26%)
# Likes:    598
# Dislikes: 0
# Total Accepted:    74.8K
# Total Submissions: 122K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。
# 
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
# 
# 
# 
# 示例：
# 
# 给你这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 
# 
# 说明：
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2:
            return head
        # 设置临时头结点    
        p_head = ListNode(0)
        p_head.next = head
        p_t = p_head
        p_t1 = p_head
        
        while True:
            cnt = 0
            while cnt < k and p_t1.next is not None:
                p_t1 = p_t1.next
                cnt += 1
            # 如果剩余节点数不够k，则退出
            if cnt < k:
                break
            
            for i in range(k-1):
                p_t2 = p_t.next
                p_t.next = p_t2.next
                p_t2.next = p_t1.next
                p_t1.next = p_t2
            for i in range(k-1):
                p_t1 = p_t1.next
            p_t = p_t1

        return p_head.next

# @lc code=end

