class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(0,n):
            for j in range(i,n):
                if abs(i-j) >= indexDifference and abs(nums[i]-nums[j])>= valueDifference:
                    return [i,j]

        return [-1,-1]
