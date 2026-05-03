# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        values = []
        queue = deque([root])
        while queue : # O(n)
            node = queue.popleft()
            values.append(node.val)
            if node.left : 
                queue.append(node.left)
            if node.right : 
                queue.append(node.right)

        values.sort() # BST property -> sorted order gives closest neighbors 

        mini = float('inf')
        for i in range(1, len(values)):
            mini = min(mini, values[i] - values[i-1])

        return mini