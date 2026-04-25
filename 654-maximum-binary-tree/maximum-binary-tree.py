# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        if not nums : 
            return 

        maximum = max(nums)
        root = TreeNode(val=maximum)

        maxindex = nums.index(maximum)
        
        root.left = self.constructMaximumBinaryTree(nums[:maxindex])
        
        root.right = self.constructMaximumBinaryTree(nums[maxindex+1:])

        return root 






        