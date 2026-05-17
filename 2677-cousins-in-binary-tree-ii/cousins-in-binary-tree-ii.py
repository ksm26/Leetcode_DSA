# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        levels = defaultdict(list)
        siblingsum = defaultdict(int)
        level = 0 
        siblingsum[1] = 0 

        while queue : 
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                levels[level].append(node.val)
                leftval = rightval = 0 

                if node.left :
                    leftval = node.left.val
                    queue.append(node.left)
                
                if node.right :
                    rightval = node.right.val
                    queue.append(node.right)

                if node.left :
                    siblingsum[node.left] = leftval + rightval
                if node.right :
                    siblingsum[node.right] = leftval + rightval
                
        
        queue = deque([root])
        level = 0 
        root.val = 0 

        while queue : 
            level += 1 

            for _ in range(len(queue)):
                node = queue.popleft()

                if node != root:
                    node.val = sum(levels[level]) - siblingsum[node]

                if node.left :
                    queue.append(node.left)
                
                if node.right :
                    queue.append(node.right)

        return root