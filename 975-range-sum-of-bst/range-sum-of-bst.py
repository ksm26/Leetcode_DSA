# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque([root])
        count = 0 

        while queue : 
            num_nodes = len(queue)

            for _ in range(num_nodes):
                node = queue.popleft()
                if (node.val >= low) and (node.val <= high):
                    count += node.val

                if node.val > low and node.left : 
                    queue.append(node.left)
                if node.val < high and node.right :
                    queue.append(node.right)

        return count
