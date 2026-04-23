# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node,curr, nodelist):
            if not node :
                return 

            # add current node
            curr += node.val 
            nodelist.append(node.val)
            
            
            # check leaf node 
            if node.left == None and node.right == None :
                if curr == targetSum:
                    result.append(nodelist[:])

            # going deeper
            left = dfs(node.left,curr, nodelist)
            right = dfs(node.right, curr, nodelist)
            
            # backtraking 
            nodelist.pop()


        dfs(root,0, [])
        return result