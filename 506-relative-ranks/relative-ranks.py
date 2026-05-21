from heapq import *
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hashmap = {}
        n = len(score)

        scores = score[:]
        for s in range(n):
            hashmap[scores[s]] = s 

        result = [0]*n

        heapify(scores)
        rank = n 

        while scores:
            num = heappop(scores)
            idx = hashmap[num]
            if rank == 1  :
                result[idx] = "Gold Medal"
            elif rank == 2  :
                result[idx] = "Silver Medal"
            elif rank == 3  :
                result[idx] = "Bronze Medal"
            else : 
                result[idx] = str(rank)
            rank -= 1 


        return result 

