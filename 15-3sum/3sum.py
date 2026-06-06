from collections import defaultdict
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        n = len(nums)

        for i in range(n):
            if nums[i] > 0 : 
                break 

            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr = nums[i]

            l = i + 1
            r = n-1

            while r > l : 
                n1 = nums[l]
                n2 = nums[r]

                if (n1 + n2 == -curr) : 
                    res.append([curr,n1,n2])
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1 
                elif n1 + n2 < -curr:
                    l += 1 
                else : 
                    r -= 1 
                
        return res

            


        
