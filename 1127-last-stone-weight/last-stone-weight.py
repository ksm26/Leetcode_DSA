from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]

        heapify(stones)

        while len(stones) > 1 :
            first = abs(heappop(stones))
            second = abs(heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        return -stones[0] if stones else 0 
        