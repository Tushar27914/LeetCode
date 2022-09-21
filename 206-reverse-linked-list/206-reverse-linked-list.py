# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currp=head
        nextp=prevp=None
        while currp!=None:
            nextp=currp.next
            currp.next=prevp
            prevp=currp
            currp=nextp
        
        self.head=prevp
        return self.head
        
        