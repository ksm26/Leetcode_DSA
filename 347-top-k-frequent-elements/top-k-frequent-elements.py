from collections import Counter
from heapq import * 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # numdict = Counter(nums) # O(n)
        # result = []

        # count = 0 
        # while count < k : # O(k)
        #     maxvalue = max(numdict.values()) # O(m)
        #     for key in numdict:
        #         if numdict[key] == maxvalue:
        #             result.append(key)
        #             break

        #     del numdict[key]
        #     count += 1 

        # return result  # O(n + k*m )
        counts = Counter(nums)
        heap = []

        for key,v in counts.items():
            heappush(heap,(v,key))
            if len(heap) > k : 
                heappop(heap)

        return [pair[1] for pair in heap]
        