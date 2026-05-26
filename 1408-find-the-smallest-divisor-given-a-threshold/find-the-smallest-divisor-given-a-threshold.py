class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def divisor(k):
            total = 0 
            for n in nums:
                total += math.ceil(n/k)


            return total <= threshold

        l = 1 
        r = max(nums)

        while l <= r : 
            k = (l+r)//2
            if divisor(k):
                r = k-1 
            else : 
                l = k +1 

        return l 

        