from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for arr in nums : # O(n)
            for x in arr : # O(n)
                counts[x] += 1 # O(1)

        n = len(nums)
        ans = []
        for key in counts : # O(n)
            if counts[key] == n : # O(1)
                ans.append(key)

        return sorted(ans) # O(n * logn)
        