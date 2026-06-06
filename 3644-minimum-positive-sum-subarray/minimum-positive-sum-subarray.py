class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minsum = float('inf')
        curr = 0 

        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i] + prefix[-1])

        for length in range(l,r+1):

            for start in range(len(nums)-length+1):
                end = start + length -1
                if start == 0 : 
                    s = prefix[end]
                else : 
                    s = prefix[end] - prefix[start-1]
                
                if s > 0 : 
                    minsum = min(minsum,s)

        return minsum if minsum!= float('inf') else -1

        