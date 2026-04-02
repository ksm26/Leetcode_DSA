from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numdict = Counter(nums)
        maxunique = -1

        for key in numdict : 
            if numdict[key] == 1 :
                maxunique = max(maxunique,key)

        return maxunique 
        