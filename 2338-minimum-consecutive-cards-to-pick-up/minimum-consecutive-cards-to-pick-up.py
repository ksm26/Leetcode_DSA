from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        cardict = defaultdict(list)
        count = float("inf")
        for i in range(len(cards)):
            num = cards[i]
            cardict[num].append(i)

        for key in cardict :
            arr = cardict[key]
            for i in range(len(arr)-1):
                count = min(count, arr[i+1]-arr[i] + 1 )

        return count if count < float("inf") else -1



        



        