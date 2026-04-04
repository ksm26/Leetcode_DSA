
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = set()

        for num in nums:
            if num < k:
                return -1

        for num in nums:
            if num > k :
                result.add(num)

        return len(result)