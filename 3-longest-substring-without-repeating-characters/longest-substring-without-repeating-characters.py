from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        count = 0 
        l = 0

        for r in range(len(s)):
            ch = s[r]
            if ch in seen :
                l = max(l, seen[ch]+1)
            seen[ch] = r
            count = max(count, r-l + 1)
        
        return count


        