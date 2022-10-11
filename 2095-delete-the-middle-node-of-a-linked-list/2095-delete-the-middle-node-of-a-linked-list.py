# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return None
        fast=head.next.next
        slow=head
        #dummy_node=ListNode(-1)
        #dummy_node.next=head
        #curr_node=dummy_node
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
            #curr_node=curr_node.next
           # if(fast.next==None and fast==None):
               # curr_node.next=curr_node.next.next
       
        return head
        