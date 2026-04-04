class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []

        i = 1

        for j in range(n//2):
            result.append(i)
            result.append(-i)
            i+=1 
        
        if n %2 !=0 :
            result.append(0)

        return result