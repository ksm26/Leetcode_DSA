class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}

        for i in range(len(nums)):
            num = nums[i]
            if target - num in hashmap.keys():
                return [i , hashmap[target-num]]

            hashmap[num] = i
        return [-1,-1]



        