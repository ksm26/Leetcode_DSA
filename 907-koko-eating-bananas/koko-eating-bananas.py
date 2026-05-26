class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def k_works(k):
            hrs = 0 
            for p in piles : 
                hrs += math.ceil(p/k)

            return hrs <= h 
        left = 1 
        right = max(piles) # max speed of eating possible

        # implement this as a binary search 
        while left < right :
            k = (left+right)//2
            if k_works(k):
                right = k
            else : 
                left = k + 1 

        return right 

        # time : O ( n * log(max(piles)))





        