from heapq import *
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        num =   [-int(ch) for ch in nums]
        heapify(num)

        for _ in range(k):
            x = heappop(num)
        
        return str(-x)


        