# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head == None):
            return head
        fast=head
        count=0
        while(fast!=None):
            count +=1
            fast = fast.next
        k = k%count
        if(k == 0):
            return head;
        slow = head 
        count = count-k-1
        while(count):
            slow = slow.next
            count -= 1
        fast = initialNode = slow.next
        slow.next = None
        while(fast.next):
            fast = fast.next
        fast.next = head
        head = initialNode
        return head
        