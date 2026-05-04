from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            stack = [node]
            while stack : 
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen : 
                        seen.add(neighbor)
                        stack.append(neighbor)        
        
        n= len(isConnected) # no of nodes
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] :
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                ans += 1 
                seen.add(i)
                dfs(i)

        return ans 

        