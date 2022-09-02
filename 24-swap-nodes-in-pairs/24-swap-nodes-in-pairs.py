# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        temp=0
        if head is None:
            return None
        if head.next is None:
            return head
        while fast!=None and fast.next!=None:
            temp=fast.val
            fast.val=fast.next.val
            fast.next.val=temp
            
            fast=fast.next.next
        return head
        
        