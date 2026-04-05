class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        seen = set(nums) # O(n)
        count = 0 
        # for i in seen: # O(n)
        #     if i != 0 :
        #         count += 1 

        # return count
        return len((seen)  - {0})