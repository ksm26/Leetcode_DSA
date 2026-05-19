# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        queue = deque([root])
        parent = {root:None}
        last_level = []
 

        while queue : 

            last_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                last_level.append(node)

                if node.left : 
                    parent[node.left] = node
                    queue.append(node.left)

                if node.right : 
                    parent[node.right] = node
                    queue.append(node.right)

        #deepets leaves are in last level 
        ancestors= set()

        node = last_level[0]
        while node : 
            ancestors.add(node)
            node = parent[node]

        for leaf in last_level[1:]:
            current_ancestor = set()
            node = leaf 
            while node : 
                current_ancestor.add(node)
                node = parent[node]
            
            ancestors= ancestors.intersection(current_ancestor)

        # return deepest ancestor 
        deepest = None 
        max_depth = -1 

        for node in ancestors:
            depth = 0 
            temp = parent[node]

            while temp : 
                depth += 1 
                temp = parent[temp]
            if depth > max_depth : 
                max_depth = depth 
                deepest = node

        return deepest 