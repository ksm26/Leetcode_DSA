from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numdict = Counter(nums)
        output = []

        for k,v in numdict.items():
            if v > 1 :
                output.append(k)
                break

        n = len(nums)
        
        for i in range(1,n+1):
            if i not in numdict:
                output.append(i)

        return output

