# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None       
        s, f = head, head
        tmp = None
        for _ in range(n):
            f = f.next
        
        while f :
            tmp = s
            s = s.next
            f = f.next
            
        tmp.next=s.next
        s.next=None
        return head
        