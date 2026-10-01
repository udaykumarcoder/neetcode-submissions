# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        l=0
        while curr:
            curr=curr.next
            l=l+1
        if n>l:
            return head
        if l==1:
            return None
            
        t_idx=l-n
        curr=head
        if t_idx==0:
                head=head.next
                return head
        if l>2:
            while t_idx-1>0:
                curr=curr.next
                t_idx-=1
            
            temp=curr.next.next
            curr.next=temp
            return head
        else:
            
            while t_idx-1>0:
                curr=curr.next
                t_idx-=1
            curr.next=None
            return head


