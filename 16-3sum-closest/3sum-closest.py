class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n-2):
            l = i + 1 
            r = n -1 

            while l < r : 
                t = nums[l] + nums[r] + nums[i]

                if abs(target-t) < abs(target-result):
                    result = t
                
                if t == target : 
                    return target 

                elif t < target : 
                    l += 1 
                else : 
                    r -= 1 

        return result


        