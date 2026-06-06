# from heapq import *
# import math
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         heap = []
#         for p in points : 
#             d= abs(math.sqrt(p[1]**2 + p[0]**2))

#             heappush(heap,(-d,p))

#             if len(heap) > k :
#                 heappop(heap)



#         return  [point for _,point in heap]

from heapq import *
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for p in points : 
            d = p[0]**2 + p[1]**2
            heappush(heap, (d,p))
        
        result = []
        for _ in range(k):
            result.append(heappop(heap)[1])

        return result