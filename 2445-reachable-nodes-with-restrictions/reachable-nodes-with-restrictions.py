class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        # graph construction 
        graph = defaultdict(list)
        for u,v in edges : 
            graph[u].append(v)
            graph[v].append(u)

        stack = [0]
        seen = set()
        seen.add(0)
        restricted_set = set(restricted)

        # performing DFS
        while stack :  # O(n)
            node = stack.pop()

            for neighbor in graph[node]:
                if neighbor not in restricted_set: # O(1)
                    if neighbor not in seen : # O(n)
                        seen.add(neighbor)
                        stack.append(neighbor)

        return len(seen)
        