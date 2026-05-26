# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = 0
        i=1
        while l1:
            d1 += i * l1.val
            i *= 10
            l1 = l1.next
        d2 = 0
        i=1
        while l2:
            d2 += i * l2.val
            i *= 10
            l2 = l2.next
        
        total = d1+d2
        if total == 0: return ListNode()
        dummy = ListNode()
        cur = dummy
        while total > 0:
            cur.next = ListNode(total % 10)
            cur = cur.next
            total = total // 10
        return dummy.next