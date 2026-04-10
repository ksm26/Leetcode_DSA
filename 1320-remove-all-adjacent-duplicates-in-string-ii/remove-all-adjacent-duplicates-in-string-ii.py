class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s : 

            # check for the duplicates in stack 
            if stack and ch == stack[-1][0]:
                stack[-1][1] += 1 
                if stack[-1][1] == k :
                    stack.pop()
            else : 
                stack.append([ch,1])
        
        ans = ""
        for i in stack :
            ans += i[0]*i[1]
        
        return ans 

        

        