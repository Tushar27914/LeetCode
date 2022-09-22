# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=1
        while curr.next!=None:
            curr=curr.next
            count+=1
        k=count-n+1
        if(k==1):
            head=head.next
            return head
        else:
            curr=head
            prev=head
            for i in range(1,k):
                prev=curr
                curr=curr.next
            prev.next=curr.next
        return head
        # curr=head
        # count=1
        # while curr.next!=None:
        #     curr=curr.next
        #     count+=1
        # k=count-n+1
        # if k==1:
        #     head=head.next
        #     return head
        # else:
        #     curr=head
        #     prev=head
        #     for i in range(1,k):
        #         prev=curr
        #         curr=curr.next
        #     prev.next=curr.next
        #     return head
                
        # curr=head
        # count=1
        # while curr.next!=None:
        #     curr=curr.next
        #     count+=1
        # k=count-n+1
        # if(k==1):
        #     head=head.next
        #     return head
        # else:
        #     curr=head
        #     prev=head
        #     for i in range(1,k):
        #         prev=curr
        #         curr=curr.next
        #     prev.next=curr.next
        #     return head