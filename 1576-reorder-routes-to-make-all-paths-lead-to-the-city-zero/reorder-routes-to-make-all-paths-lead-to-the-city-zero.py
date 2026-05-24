class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        roads = set()
        graph = defaultdict(list)
        for u,v in connections : 
            graph[u].append(v)
            graph[v].append(u)
            roads.add((u,v)) # adding original edges into a set
        
        stack = [0]
        ans = 0 
        seen = {0}

        while stack : 
            node = stack.pop()

            for neighbor in graph[node]:
                if neighbor not in seen : 
                    if (node,neighbor) in roads : 
                        ans += 1 
                    seen.add(neighbor)
                    stack.append(neighbor)

        return ans 


        

        
        