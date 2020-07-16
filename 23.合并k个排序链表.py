#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (51.77%)
# Likes:    696
# Dislikes: 0
# Total Accepted:    127.6K
# Total Submissions: 246.5K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while None in lists:
            lists.remove(None)
        if len(lists) == 0:
            return None
        
        pHead = ListNode(0)#空节点
        pTmp = pHead
        
        while True:
            min_pos = 0
            for cnt1 in range(len(lists)):
                if lists[cnt1].val < lists[min_pos].val:
                    min_pos = cnt1
            else:
                pTmp.next = lists[min_pos]
                pTmp = pTmp.next
                if lists[min_pos].next is None:
                     lists.pop(min_pos)
                     if len(lists) == 0:
                        break
                else:
                    lists[min_pos] = lists[min_pos].next
                                 
        return pHead.next

# @lc code=end

