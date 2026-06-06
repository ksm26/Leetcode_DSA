class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        heap = []
        heapify(heap)
        mat = []

        for row in matrix : 
            mat = mat + row

        mat.sort()

        return mat[k-1]




        