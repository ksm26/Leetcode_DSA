class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result = []
        for row in matrix : 
            count = row.count(1)

            result.append(count)

        return result