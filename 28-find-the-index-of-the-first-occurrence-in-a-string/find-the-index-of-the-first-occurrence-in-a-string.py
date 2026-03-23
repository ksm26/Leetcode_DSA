class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0 

        k = len(needle) # O(1)
        for i in range(len(haystack)-k + 1): # O(n-k+1) ~ O(n)
            if needle == haystack[i:i+k]: # O(k)
                return i 

        return -1 
# Total: O(n * k)


        

        