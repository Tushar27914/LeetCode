# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        head1=dummy
        for i in range(m-1):
            head1=head1.next
        p=head1.next
        for j in range(n-m):
            temp=head1.next
            head1.next=p.next
            p.next=p.next.next
            head1.next.next=temp
        return dummy.next
        
#    # def reverseBetween(self, head, m, n):
#         dummy = pre = ListNode(0)
#         dummy.next = head

#     # reach the (m-1)th node
#         for _ in range(m-1):
#             pre = pre.next
        
#     # Reverse m to n
#         curr = pre.next
#         node = None
#         for _ in range(n-m+1):
#             tmp = curr.next
#             curr.next = node
#             node = curr
#             curr = tmp
        
#     # Connect m to n+1 and m-1 to n
#         pre.next.next = curr
#         pre.next = node
#         return dummy.next
        
        
        # dummy = ListNode(0)
        # dummy.next=  head 
        # head1 = dummy
        # for i in range(left-1):
        #     head1 = head1.next 
        # p = head1.next 
        # for j in range(right-left):
        #     temp = head1.next 
        #     head1.next = p.next
        #     p.next = p.next.next
        #     head1.next.next = temp 
        # return dummy.next 