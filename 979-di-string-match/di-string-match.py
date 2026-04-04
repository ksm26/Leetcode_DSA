class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = []
        lo = 0 
        h = len(s)
        n = len(s)
        for i in range(0,n):
            if s[i] == "I":
                ans.append(lo)
                lo += 1
            else :
                ans.append(h)
                h -= 1 

        return ans + [lo]

        