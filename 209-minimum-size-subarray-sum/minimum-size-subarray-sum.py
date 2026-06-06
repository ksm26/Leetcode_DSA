class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0 

        minlen = float('inf')
        l = 0 
        for r in range(len(nums)):
            curr += nums[r]
            while curr>= target:
                minlen = min(minlen, r-l+1)
                curr -= nums[l]
                l += 1 
        return minlen if minlen!= float('inf') else 0 


            
        