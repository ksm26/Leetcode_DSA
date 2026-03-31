class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixsum = [nums[0]]
        for i in range(1,n):
            prefixsum.append(nums[i]+prefixsum[-1])

        if prefixsum[-1] == prefixsum[0]:
            return 0 
        
        for i in range(1,n):
            left = prefixsum[i-1]
            right = prefixsum[-1] - prefixsum[i]
            if left == right :
                return i 

        return -1 
        