# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        middle = None
        list1 = head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        list2 = middle.next
        middle.next = None
        #2 lists made
        #Reversing second list
        list2 = self.reverseList(list2)
        temp = None
        count = 0
        while list1 and list2:
            if count % 2 == 0:
                temp = list1.next
                list1.next = list2
                list1 = temp
            elif count % 2 == 1:
                temp = list2.next
                list2.next = list1
                list2 = temp
            count += 1
        # print(f"Head Value is {head.val}")
        # return head
        
            



            



        