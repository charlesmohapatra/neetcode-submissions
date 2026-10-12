# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.answer = []
        curr = root
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.answer.append(curr.val)
                curr = curr.right

        self.pointer = -1

    def next(self) -> int:
        self.pointer += 1
        return self.answer[self.pointer]

        

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.answer)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()