class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        area = 0 

        while left <=right:
            if height[left] <= height[right]:
                curr = height[left] * abs(right-left)
                left += 1
            elif height[left] > height[right]:
                curr = height[right] * abs(right-left)
                right -=1 

            area = max( area, curr)
        return area

        