# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        lenght=1
        lastelement=head
        while lastelement.next!=None:
            lastelement=lastelement.next
            lenght+=1
        k=k%lenght
        lastelement.next=head
        tempnode=head
        for i in range(lenght-k-1):
            tempnode=tempnode.next
        ans=tempnode.next
        tempnode.next=None
        return ans
        
        
      
  
        