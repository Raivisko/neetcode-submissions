# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next: return None
        dummy = ListNode(0, head)
        s, f = dummy, dummy   
        tmp = None
        for _ in range(n):
            f = f.next
        
        while f and f.next :
            tmp = s
            s = s.next
            f = f.next
        # return f.val
        s.next=f
        s=f
        return dummy.next
        