# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        prev = dummy
        curr = head

        while curr :
            # if current node is duplicate 
            if curr.next and curr.val == curr.next.val :
                # move to last duplicated node
                while curr.next  and curr.val == curr.next.val:
                    curr = curr.next

                # skip duplicated node
                prev.next = curr.next
            else :
                # keep moving forward
                prev = prev.next

            curr = curr.next
        
        return dummy.next

        
        