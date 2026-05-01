# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        def traverse(root):
            if not root : 
                return []
            list1 = []
            queue = deque([root])
            while queue :
                node = queue.popleft()
                list1.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)

            return list1

        list1= traverse(root1)
        list2 = traverse(root2)
        list1 = list1 + list2 
        list1.sort()

        return list1


        