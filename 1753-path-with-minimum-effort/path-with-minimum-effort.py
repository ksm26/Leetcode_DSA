class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(r,c):
            return 0<= r < m and 0<= c < n 

        def check(efforts):
            directions = {(0,1),(1,0),(0,-1),(-1,0)}
            seen = {(0,0)}
            stack = [(0,0)]

            while stack : 
                r,c = stack.pop()
                if (r,c) == (m-1,n-1):
                    return True
                for dr,dc in directions : 
                    new_r, new_c = r + dr, c + dc 
                    if valid(new_r, new_c) and (new_r, new_c) not in seen:
                        if abs(heights[r][c] - heights[new_r][new_c]) <= efforts :
                            seen.add((new_r,new_c))
                            stack.append((new_r,new_c))

            return False

        m = len(heights)
        n = len(heights[0])
        left = 0 
        right = max(max(row) for row in heights)

        # for efforts from left val to right val 
        while left <= right : 
            mid = (left + right) // 2 
            if check(mid):
                right = mid - 1
            else : 
                left = mid + 1 

        return left