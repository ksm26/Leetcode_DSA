from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # balloon = Counter("balloon")
        # string = Counter(text)
        # times = float("inf")

        # for ch in balloon : 
        #     available = string.get(ch,0)
        #     needed = balloon[ch]
        #     times = min(times, available //needed)

        # return times 
        return min(text.count("b"), text.count("a"),text.count("l")//2,text.count("o")//2,text.count("n"))




        