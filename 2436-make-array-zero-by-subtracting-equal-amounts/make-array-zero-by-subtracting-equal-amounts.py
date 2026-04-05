class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        seen = set(nums)
        count = 0 
        for i in seen:
            if i != 0 :
                count += 1 

        return count