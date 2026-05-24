class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges : 
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        total_comp = 0 

        for i in range(n):
            if i not in visited : 
                stack = [i]
                visited.add(i)
                nodes = 0
                edges = 0 
                while stack : 
                    node = stack.pop()
                    nodes += 1
                    edges += len(graph[node])

                    for ngbr in graph[node]:
                        if ngbr not in visited:
                            visited.add(ngbr)
                            stack.append(ngbr)

                actual_edges = edges // 2 
                expected_edges = nodes *(nodes -1 ) // 2
                if actual_edges == expected_edges : 
                    total_comp += 1 

        return total_comp
