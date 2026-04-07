# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return None

        stk = []
        while head != None:
            stk.append(head)
            head = head.next
        
        new_head = stk.pop()
        cur = new_head
        while len(stk) > 0:
            cur.next = stk.pop()
            cur = cur.next
        cur.next = None
        
        return new_head