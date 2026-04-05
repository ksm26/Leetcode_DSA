from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0 
        count = 0 
        maxsum= 0

        for r in range(len(nums)):
            num = nums[r]
            count += num
            while num in seen:
                seen.remove(nums[l])
                count -= nums[l]
                l += 1
            seen.add(num)
            maxsum = max(maxsum,count)
        
        return maxsum        