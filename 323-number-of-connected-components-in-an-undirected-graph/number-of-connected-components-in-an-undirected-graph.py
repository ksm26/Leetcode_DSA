class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        ans = 0 

        for node in range(n):

            if node not in seen : 
                stack = [node]
                seen.add(node)

                while stack : 
                    curr = stack.pop()
                    for neighbor in graph[curr]:
                        
                        if neighbor not in seen:
                            seen.add(neighbor)
                            stack.append(neighbor)

                ans += 1 

        return ans


        