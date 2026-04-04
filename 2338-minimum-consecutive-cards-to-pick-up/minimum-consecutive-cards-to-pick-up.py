from collections import defaultdict
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        # cardict = defaultdict(list)
        # count = float("inf")
        # for i in range(len(cards)): # O(n)
        #     num = cards[i]
        #     cardict[num].append(i)

        # for key in cardict :  # O(k)
        #     arr = cardict[key]
        #     for i in range(len(arr)-1):  # O(m)
        #         count = min(count, arr[i+1]-arr[i] + 1 )

        # return count if count < float("inf") else -1  # O(k*m)

        cardict = {}
        count = float("inf")
        for i in range(len(cards)):
            num = cards[i]
            if num in cardict:
                count = min(count, i - cardict[num] + 1)
                cardict[num] = i 
            else : 
                cardict[num] = i 

        return count if count < float("inf") else -1



        



        