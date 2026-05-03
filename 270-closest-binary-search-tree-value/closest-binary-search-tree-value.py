# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        queue = deque([root])
        closest = root.val

        while queue : 
            node = queue.popleft()

            # update closest value
            if abs(node.val - target) < abs(closest - target) or (abs(node.val - target) == abs(closest-target) and node.val < closest):
                closest = node.val

            if node.left : 
                queue.append(node.left)
            if node.right : 
                queue.append(node.right)

        return closest

