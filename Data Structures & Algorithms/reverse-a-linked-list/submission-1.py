# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev, curr =  None, head
            while curr:
                next1 = curr.next
                curr.next = prev
                prev = curr
                curr = next1
            return prev
        else:
            return head
        


        
        