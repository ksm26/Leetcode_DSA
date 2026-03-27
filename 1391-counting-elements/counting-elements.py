class Solution:
    def countElements(self, arr: List[int]) -> int:

        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i]+= 1
            else : 
                hashmap[i] = 1 

        count = 0 
        for i in arr :
            if (i+1) in hashmap and i in hashmap :
                count += 1

        return count