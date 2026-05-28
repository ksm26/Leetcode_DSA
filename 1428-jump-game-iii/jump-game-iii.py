class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)-1

        def valid(idx):
            return 0<= idx<= n 

        queue = deque([start])
        seen = {start}

        while queue : 
            idx = queue.popleft()

            if valid(idx):
                if arr[idx] == 0 :
                    return True
            
            if valid(idx-arr[idx]) : 
                if (idx - arr[idx]) not in seen : 
                    seen.add(idx-arr[idx])
                    queue.append(idx-arr[idx])
            
            if valid(idx+arr[idx]) : 
                if (idx + arr[idx]) not in seen : 
                    seen.add(idx+arr[idx])
                    queue.append(idx+arr[idx])

        return False

        