class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop = popped[0]
        left = 0 

        for x in pushed:
            stack.append(x)

            while stack and left < len(popped) and stack[-1] == popped[left]:
                stack.pop()
                left += 1 
        
        return not stack
            
        