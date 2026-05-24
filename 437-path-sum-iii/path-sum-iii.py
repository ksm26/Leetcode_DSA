# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0 
        if not root : 
            return 0 

        stack = [(root, [root.val])]
        while stack : 
            node, path = stack.pop()

            # check all suffix sum 
            curr_sum = 0
            for i in range(len(path)-1,-1,-1):
                curr_sum += path[i]
                if curr_sum == targetSum:
                    count += 1

            if node.left :
                stack.append((node.left, path + [node.left.val]))

            if node.right :
                stack.append((node.right, path + [node.right.val]))

        return count 
            
        