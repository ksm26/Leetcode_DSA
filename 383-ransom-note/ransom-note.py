from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        ransom = Counter(ransomNote)

        for ch in ransom : 
            if not ch in mag or ransom[ch] > mag[ch]:
                return False
        return True 