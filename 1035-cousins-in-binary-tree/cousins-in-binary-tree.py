# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        queue = deque([root])
        level = 0 
        levelnodes = defaultdict(list)
        parent = {}

        while queue : 
            level +=1 
            for _ in range(len(queue)):
                node = queue.popleft()
                levelnodes[level].append(node.val)

                if node.left : 
                    parent[node.left.val] = node.val
                    queue.append(node.left)

                if node.right : 
                    parent[node.right.val] = node.val
                    queue.append(node.right)

        for k, val in levelnodes.items():
            if x in val and y in val :
                if parent[x] != parent[y]:
                    return True

        return False