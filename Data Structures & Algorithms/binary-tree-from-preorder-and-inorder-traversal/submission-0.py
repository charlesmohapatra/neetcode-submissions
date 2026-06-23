# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootNode = TreeNode(preorder[0])
        root = rootNode.val
        inorder_root_index = inorder.index(root)
        #inorder elements
        left_inorder_array = inorder[0:inorder_root_index]
        right_inorder_array = inorder[inorder_root_index+1:]

        length_left_inorder = len(left_inorder_array)
        length_right_inorder = len(right_inorder_array)

        #preorder elements
        left_preorder_array = preorder[1:1+length_left_inorder]
        right_preorder_array = preorder[1+length_left_inorder:]

        rootNode.left = self.buildTree(left_preorder_array, left_inorder_array)
        rootNode.right = self.buildTree(right_preorder_array, right_inorder_array)
        return rootNode


        