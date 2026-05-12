from collections import defaultdict
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        for word in words1 : 
            map1[word] += 1 
        
        for word in words2 : 
            map2[word] += 1 

        common = 0 
        for word in map1:
            if map1[word] == 1 : 
                if map2[word] == 1 :
                    common += 1

        return common 
