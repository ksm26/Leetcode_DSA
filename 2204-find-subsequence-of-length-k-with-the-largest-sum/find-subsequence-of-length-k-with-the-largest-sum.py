class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        heapify(heap)
        n = len(nums)

        for i in range(n):
            heappush(heap,(nums[i],i))
            if len(heap) > k :
                heappop(heap)

        heap.sort(key= lambda x: x[1])
        return [pair[0] for pair in heap]

        