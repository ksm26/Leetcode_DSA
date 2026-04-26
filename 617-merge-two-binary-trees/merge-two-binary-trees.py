# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def merge(r1,r2):
            if not r1:
                return r2
            if not r2:
                return r1 
            
            node = TreeNode(r1.val + r2.val)
            node.left = merge(r1.left, r2.left)
            node.right = merge(r1.right, r2.right)

            return node


        return merge(root1,root2)
