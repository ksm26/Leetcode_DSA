# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessdummy = ListNode(0) # dummy heads
        largedummy = ListNode(0)

        less = lessdummy # dummy pointers
        large = largedummy

        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            elif curr.val >= x :
                large.next = curr
                large  = large.next

            curr = curr.next
        
        large.next = None        
        less.next = largedummy.next

        return lessdummy.next