# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []

        ans = []

        queue = deque([root])
        while queue:
            curr_len = len(queue)
            currmax = float('-inf')
            for _ in range(curr_len):
                node = queue.popleft()
                currmax = max(currmax,node.val)

                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            ans.append(currmax)

        return ans
        