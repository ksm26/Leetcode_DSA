class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans = 0 
        prefix = [nums[0]]

        for i in range(1,len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        count = 0 
        for i in range(len(nums)-1):
            left = prefix[i]
            right = prefix[-1] - prefix[i]
            if left >= right : 
                count += 1 

        return count 
        