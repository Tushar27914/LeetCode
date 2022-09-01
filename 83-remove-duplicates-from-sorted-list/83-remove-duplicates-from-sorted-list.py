# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result=head
        if head is None:
            return None
        while result.next is not None:
            if result.val==result.next.val:
                result.next=result.next.next
            else:
                result=result.next
        return head
        
        