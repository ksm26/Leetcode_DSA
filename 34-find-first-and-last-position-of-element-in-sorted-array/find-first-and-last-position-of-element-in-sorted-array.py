class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first():
            l = 0 
            r = len(nums) - 1 
            first = -1

            while l <= r : 
                mid = (l+r)//2

                if nums[mid] == target:
                    first = mid
                    r = mid -1 # keep searching left
                
                elif nums[mid] > target : 
                    r = mid - 1 

                else :
                    l = mid + 1 

            return first

        def last():
            l = 0 
            r = len(nums) - 1 
            last = -1

            while l <= r : 
                mid = (l+r)//2

                if nums[mid] == target:
                    last = mid
                    l = mid + 1 # keep searchign right
                
                elif nums[mid] > target : 
                    r = mid - 1 

                else :
                    l = mid + 1 

            return last

        return [first(),last()]
        