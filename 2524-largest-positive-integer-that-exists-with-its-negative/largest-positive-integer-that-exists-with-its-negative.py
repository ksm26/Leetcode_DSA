from collections import Counter
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numdict = Counter(nums)
        maximum = -1 
        for i in nums :
            if -i in numdict:
                maximum = max(maximum, abs(i))
        
        return maximum