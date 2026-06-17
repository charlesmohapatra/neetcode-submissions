# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = None
        head = None
        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif not list1 and not list2:
            return list1
        while list1 and list2:
            if list1.val <= list2.val:
                if not curr:
                    curr = list1
                    head = curr
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if not curr:
                    curr = list2
                    head = curr
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
            if list1:
                curr.next = list1
            else:
                curr.next = list2
        return head
            