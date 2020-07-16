#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (37.27%)
# Likes:    4257
# Dislikes: 0
# Total Accepted:    403.1K
# Total Submissions: 1.1M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_res = ListNode((l1.val+l2.val)%10)
        temp = l_res
        f_add = (l1.val+l2.val)//10#int(l1.val+l2.val >= 10)
        while l1.next or l2.next:
            #在判断是否为None的时候，不要加 “！=None”，可以提高速度 
            num1 = 0
            num2 = 0       
            if l1.next:
                l1 = l1.next
                num1 = l1.val
            if l2.next:
                l2 = l2.next
                num2 = l2.val
                
            temp.next = ListNode((num1+num2+f_add)%10)
            temp = temp.next
            f_add = (num1+num2+f_add)//10#int((num1+num2+f_add)>=10)
        if f_add:
            temp.next = ListNode(1)

        return l_res
# @lc code=end

