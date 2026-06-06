from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        k = len(p)
        ref = Counter(p)
        wind = Counter()
        ans =  [] 

        for i in range(len(s)):
            wind[s[i]] += 1

            if i >= k : 
                wind[s[i-k]] -= 1
                if wind[s[i-k]] == 0 : 
                    del wind[s[i-k]]

            if wind == ref:
                ans.append(i-k+1)
            
        return ans





        