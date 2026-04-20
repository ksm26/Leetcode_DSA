# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        arr[k-1] , arr[len(arr)-k] = arr[len(arr)-k], arr[k-1]

        node = head
        for i in arr:
            node.val = i
            node = node.next 

        return head

        

        