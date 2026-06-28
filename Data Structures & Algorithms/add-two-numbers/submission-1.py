# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = []
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            a = ListNode(sum % 10)
            ans.append(a)
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                sum = l1.val + carry
                carry = sum // 10
                tmp= ListNode(sum % 10)
                ans.append(tmp)
                l1 = l1.next
            if carry:
                tmp = ListNode(carry)
                ans.append(tmp)
        elif l2:
            while l2:
                sum = l2.val + carry
                carry = sum // 10
                tmp= ListNode(sum % 10)
                ans.append(tmp)
                l2 = l2.next
            if carry:
                tmp = ListNode(carry)
                ans.append(tmp)
        elif carry:
            tmp = ListNode(carry)
            ans.append(tmp)

        for node in range(len(ans)):
            if node + 1 <= len(ans) - 1:
                ans[node].next = ans[node+1]
        return ans[0]


        