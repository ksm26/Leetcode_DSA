class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        destiny = set()

        for i in paths:
            source.add(i[0])
            destiny.add(i[1])
        
        for i in destiny :
            if i not in source:
                return i 
        