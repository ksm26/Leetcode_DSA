from heapq import *
import math
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        heap = [-p for p in piles]
        heapify(heap)

        for _ in range(k):
            x = heappop(heap)
            x = math.floor(x/2)
            heappush(heap,x)

        return -sum(heap)

        