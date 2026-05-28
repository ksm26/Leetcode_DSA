class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
      
        n = len(bombs)
        maxcount = 0 
        bomblist = defaultdict(list)

        for i,(x1,y1,r1) in enumerate(bombs):
            for j,(x2,y2,_) in enumerate(bombs):
                if i!=j : 
                    dx,dy = x1-x2, y1-y2
                    if dx*dx + dy*dy <= r1*r1:
                        bomblist[i].append(j)

        # BFS
        for i in range(n) :
            queue = deque([i])
            visited= set([i])

            while queue : 
                curr = queue.popleft()
                for ngbr in bomblist[curr]:
                    if ngbr not in visited:
                        visited.add(ngbr)
                        queue.append(ngbr)

            maxcount = max(maxcount , len(visited))

        return maxcount 




        