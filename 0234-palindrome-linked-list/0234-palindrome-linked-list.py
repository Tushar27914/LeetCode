# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l1=head
        a=""
        b=""
        while(l1):
            b=b+str(l1.val)
            l1=l1.next
        if(b==b[::-1]):
            return True
        else:
            return False
    
        
        