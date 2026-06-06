from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        heap = []
        heapify(heap)

        for key,v in counts.items():
            heappush(heap,(-v,key))
        
        return [heappop(heap)[1] for _ in range(k)]
        