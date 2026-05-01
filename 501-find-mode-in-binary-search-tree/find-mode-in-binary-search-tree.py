# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        hashmap ={}

        while queue :
            num_nodes = len(queue)
            for _ in range(num_nodes):
                node = queue.popleft()
                if node.val in hashmap :
                    hashmap[node.val] += 1 
                else : 
                    hashmap[node.val] = 1 
                
                if node.left : 
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
        
        maxfreq = max(hashmap.values())

        return [k for k in hashmap if hashmap[k] == maxfreq]
        