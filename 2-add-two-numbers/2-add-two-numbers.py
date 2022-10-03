# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            if l1:
                v1=l1.val #l1 value put the v1 variable
            else:
                v1=0
            if l2:
                v2=l2.val #l2 value put the v2 variable
            else:
                v2=0
            val=v1+v2+carry #both v1 and v2 or carry sum put the val variable
            carry=val//10  #find the carry
            val=val%10  # find the value
            curr.next=ListNode(val)  #put the value of the node
            curr=curr.next #point to the next node
            if l1:
                l1=l1.next #if l1 given poin to the next pointer
            else:
                l1=None
            if l2:
                l2=l2.next #if l2 given point to the next pointer
            else:
                l2=None
        return dummy.next #return to the list
                
                
                
        
