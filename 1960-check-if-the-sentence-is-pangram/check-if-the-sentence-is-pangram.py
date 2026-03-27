class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        
        for i in sentence:
            if i not in seen :
                seen.add(i)
                
        return True if len(seen)==26 else False
            