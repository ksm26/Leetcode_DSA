class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startvalue = min_value = 0 
        n = len(nums)
        for i in range(0, n):
            startvalue += nums[i]
            min_value = min(min_value, startvalue)

        return abs(min_value) + 1 

        