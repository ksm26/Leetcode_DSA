class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [nums[0]]
        for i in range(1,n):
            prefixSum.append(nums[i]+ prefixSum[-1])

        total = prefixSum[-1]
        
        for i in range(n):
            l = prefixSum[i] - nums[i]
            r = total - prefixSum[i] 
            if l == r :
                return i 

        return -1  


        