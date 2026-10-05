# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        dummy=ListNode(0)
        curr=dummy
        
        carry=0
        while curr1 or curr2 or carry:
            temp=0
            if curr1:
                temp+=curr1.val
                curr1=curr1.next
            if curr2:
                temp+=curr2.val
                curr2=curr2.next
            temp+=carry
            carry=0
            ans=temp%10
            carry=temp//10
            curr.next=ListNode(ans)
            curr=curr.next
            
        return dummy.next