# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {} # build parent map 

        queue = deque([root])
        # BFS tree traversal for storing the node values at each level
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left :
                    parent[node.left] = node
                    queue.append(node.left)
                if node.right :
                    parent[node.right] = node
                    queue.append(node.right)

        #BFS from target
        visited = set()
        queue = deque([target])
        visited.add(target)
        distance = 0 

        while queue:

            if distance == k : 
                return [node.val for node in queue]

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left and node.left not in visited:
                    visited.add(node.left)
                    queue.append(node.left)

                if node.right and node.right not in visited:
                    visited.add(node.right)
                    queue.append(node.right)
                
                if node in parent and parent[node] not in visited:
                    visited.add(parent[node])
                    queue.append(parent[node])
            distance += 1 

        return []