# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0 

        self.mindepth = float('inf')
        self.dfs(root,0)

        return self.mindepth

    def dfs(self, node, currdepth):
        if not node :
            return 
        
        if not node.left and not node.right:
            self.mindepth = min(self.mindepth, currdepth+1)
        
        self.dfs(node.left, currdepth + 1)
        self.dfs(node.right, currdepth + 1)

        

        