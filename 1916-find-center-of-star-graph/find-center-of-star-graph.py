from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        hashmap = defaultdict(list)

        for x, y in edges:
            hashmap[x].append(y)
            hashmap[y].append(x)

        for key,value in hashmap.items():
            if len(value) == len(edges):
                return key
        