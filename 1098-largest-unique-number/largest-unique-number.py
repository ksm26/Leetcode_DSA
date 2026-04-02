from collections import Counter
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numdict = Counter(nums)
        numones = []

        for key in numdict : 
            if numdict[key] == 1 :
                numones.append(key)
        if not numones : 
            return -1 

        return sorted(numones)[-1] 
        