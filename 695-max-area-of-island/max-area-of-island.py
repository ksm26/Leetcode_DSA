class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        def valid(row,col):
            return 0<= row < m and 0<= col < n and grid[row][col] == 1

        def dfs(row,col):
            stack = [(row,col)]
            area = 1 
            while stack : 
                r,c = stack.pop()
                for dr,dc in directions: 
                    newr , newc = r+dr, c+dc
                    if valid(newr,newc) and (newr,newc) not in seen: 
                        seen.add((newr,newc))
                        stack.append([newr,newc])
                        area +=1 

            return area 

        directions = {(0,1), (1,0), (0,-1), (-1,0)}
        r,c = 0,0 
        seen = set()

        max_area = 0 
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r,c) not in seen : 
                    seen.add((r,c))
                    max_area = max(max_area, dfs(r,c))

        return max_area

        