# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        stack = [(root,[root.val])]
        paths = []
        # DFS traversal 
        while stack : 
            node, path = stack.pop()

            if node.left is None and node.right is None : 
                paths.append(path) # store the paths from root to leafs

            if node.left : 
                stack.append((node.left, path+[node.left.val]))

            if node.right : 
                stack.append((node.right, path + [node.right.val]))


        total = 0 

        for p in paths:
            l = len(p)
            t= 0 
            for i in range(len(p)):
                t += p[i] * (10**(l-i-1))

            total += t 

        return total 