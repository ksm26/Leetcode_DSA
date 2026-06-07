# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # iterative 
        if not root :
            return []

        stack1, stack2 = [root], []

        while stack1 : 
            node = stack1.pop()
            stack2.append(node.val)

            if node.left :
                stack1.append(node.left)
            if node.right :
                stack1.append(node.right)

        return [val for val in reversed(stack2)]