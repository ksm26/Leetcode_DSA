class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i): # i tells where to start iterating
            if i >  len(nums):
                return 

            ans.append(curr[:]) # answers at each node 

            for j in range(i, len(nums)) : 
                curr.append(nums[j]) # add to current path
                backtrack(curr,j+1) # move to child, considering the elements that comes after this element for future cals
                curr.pop()

        ans = []
        backtrack([],0)
        return ans
        