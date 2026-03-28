class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in nums :
            if i in hashmap :
                hashmap[i] += 1 
            else : 
                hashmap[i] = 1
        ans = []
        for i in nums :
            if hashmap[i] == 1 :
                ans.append(i)
        return ans 
        