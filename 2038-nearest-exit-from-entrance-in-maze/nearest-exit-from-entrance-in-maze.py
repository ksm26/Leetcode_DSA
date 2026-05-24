class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        # initialize queue as entrance and distance as 0 
        queue = deque([(entrance[0], entrance[1], 0)])
        # mark the entrance as visited by converting it into a wall 

        maze[entrance[0]][entrance[1]] = "+"

        while queue : 
            row , col, distance = queue.popleft()

            # check if exit 
            if ( row == 0 or row == m-1 or col == 0 or col == n-1) and distance>0 : 
                return distance 

            # check all neighbor and enque them if they are empty 
            for dr, dc in directions : 
                r , c = row + dr, col + dc 

                if 0 <= r < m and 0 <= c < n and maze[r][c] == ".":
                    maze[r][c] = "+"
                    queue.append((r,c,distance + 1 ))
        
        # if we are here no path to exit 
        return -1

        