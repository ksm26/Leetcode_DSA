class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def valid(row,col):
            return 0<= row <m and 0<= col < n and grid[row][col] == "1"

        def dfs(row,col):
            for dr,dc in directions : 
                r,c = row + dr, col + dc
                if valid(r,c) and (r,c) not in seen : 
                    seen.add((r,c))
                    dfs(r,c)


        directions = {(0,1), (1,0), (-1,0), (0,-1)}
        seen = set ()
        ans = 0 
        m,n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row,col) not in seen : 
                    ans +=1 
                    seen.add((row,col))
                    dfs(row,col)


        return ans 
        