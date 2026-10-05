# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        n = len(arr)
        max_sum = -1
        for i in range(0, n//2):
            temp_sum = arr[i] + arr[n-1-i]
            max_sum = max(max_sum, temp_sum)
        return max_sum

        

        