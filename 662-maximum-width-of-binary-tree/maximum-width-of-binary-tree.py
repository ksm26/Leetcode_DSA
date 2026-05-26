# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxwidth = 0 
        queue = deque([(root,0)])

        while queue : 

            offset = queue[0][1]
            first_idx = queue[0][1] - offset
            last_idx = queue[-1][1] - offset

            maxwidth = max(maxwidth, last_idx - first_idx + 1)
            
            for _ in range(len(queue)):
                node, idx = queue.popleft()

                if node.left : 
                    queue.append((node.left, 2 * idx))
                if node.right : 
                    queue.append((node.right, 2 * idx + 1 ))

                
            

        return maxwidth
        