class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(r,c):
            return 0<= r < m and 0<= c < n and grid[r][c] == 0 
        
        m = len(grid)
        n = len(grid[0])

        directions = {(0,1), (1,0),(-1,0),(0,-1)}
        queue= deque([(0,0,k,0)])
        seen = {(0,0,k)}

        while queue : 
            r,c,remain,steps = queue.popleft()
            if r == m-1 and c == n-1 : 
                return steps 

            for dr,dc in directions : 
                new_r, new_c = r+dr, c+dc 
                
                if valid(new_r,new_c) : 
                    if (new_r,new_c, remain) not in seen : 
                        seen.add((new_r,new_c,remain))
                        queue.append((new_r,new_c,remain,steps+1))

                elif remain and  (new_r,new_c, remain-1) not in seen: 
                    seen.add((new_r,new_c,remain-1))
                    queue.append((new_r,new_c,remain-1,steps+1))
        
        return -1 

                    

        
        