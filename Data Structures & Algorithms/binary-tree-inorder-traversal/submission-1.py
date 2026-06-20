class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)
        traverse(root)
        return ans