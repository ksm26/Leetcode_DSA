class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxvalue = max(candies)

        result= [i+extraCandies >= maxvalue for i in candies]
    
        return result
        