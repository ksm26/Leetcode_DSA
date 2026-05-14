from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        nums = Counter(arr)
        seen = set()
        freq = 0 
        nums = dict(sorted(nums.items(), key =lambda item: item[1], reverse=True))

        for k,v in nums.items():
            if freq >= int(n/2):
                break
            seen.add(k)
            freq += v

        return len(seen)
