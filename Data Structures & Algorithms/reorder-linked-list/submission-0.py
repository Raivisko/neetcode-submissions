# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
        mid = slow
    
        prev, curr = None, mid
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        l, r = head, prev
        l1, r1 = l.next, r.next
        while l1 and r1:
            l.next = r
            r.next = l1
            l = l1
            r=r1
            l1 = l1.next
            r1=r1.next
        return r.next
        