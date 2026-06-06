from heapq import * 
from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(nums)
        heap = []

        for k,v in count.items():
            if k %2 == 0 : 
                heappush(heap,(-v,k))

        if not heap : 
            return -1 

        return heappop(heap)[1]
        