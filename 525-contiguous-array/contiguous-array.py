class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        prefixsum = [0]

        for num in nums : 
            if num == 0 :
                prefixsum.append(-1 + prefixsum[-1])
            elif num == 1 :
                prefixsum.append(1 + prefixsum[-1])
        
        count = 0 
        prefixdict = {}
        for i in range(len(prefixsum)):
            num = prefixsum[i]
            if num not in prefixdict : 
                prefixdict[num]= i 
            else : 
                count = max(count, i - prefixdict[num])

        return count

        
        