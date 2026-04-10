class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for f in logs :
            if stack and f == "../":
                stack.pop()
            elif f != "./"  and f !="../": 
                stack.append(f)
        
        return len(stack)
        