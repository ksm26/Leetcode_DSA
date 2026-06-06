from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapify(stones)

        while len(stones) > 1 : 
            y = abs(heappop(stones))
            x = abs(heappop(stones))
            if x!=y : 
                y = abs(y - x)
                heappush(stones,-y)

        return -stones[0] if stones else 0 


        