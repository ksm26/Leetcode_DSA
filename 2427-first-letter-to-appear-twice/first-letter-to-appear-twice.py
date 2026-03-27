class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # hashmap = {}
        # for i in s : 
        #     if i in hashmap.keys():
        #         return i 
        #     hashmap[i] = 1
        hashmap = set()
        for i in s : 
            if i in hashmap:
                return i 
            hashmap.add(i)

            
            
        