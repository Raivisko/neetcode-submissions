# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        l, r = head1, head2

        while l and r:
            if l.val<r.val:
                curr.next=l
                l=l.next
            else:
                curr.next=r
                r=r.next
            curr=curr.next

        if l:
            curr.next = l
        elif r:
            curr.next=r
        return dummy.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next