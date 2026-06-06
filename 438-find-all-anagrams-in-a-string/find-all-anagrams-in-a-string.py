from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        k = len(p)
        ref = Counter(p)
        ans =  [] 

        for i in range(len(s)-k+1):
            arr = s[i:i+k]
            count = Counter(arr)
            if count == ref:
                ans.append(i)
            
        return ans





        