class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        def speeds(s):
            hrs = 0 
            for d in dist:
                hrs = ceil(hrs)
                hrs += (d/s)

            return hrs <= hour

        l = 1
        r = 10**7

        while l <= r : 
            s = (l + r)//2
            if speeds(s):
                r = s - 1
            else : 
                l = s + 1 

        return l
