from collections import Counter
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        chemistry = 0 

        if total % (len(skill) // 2) != 0:
            return -1

        score = total //(len(skill)//2)

        numdict = Counter(skill)

        for i in skill:
            if numdict[i] == 0 :
                continue
            if i == score- i and numdict[i] < 2 :
                return -1 

            if numdict[score-i] == 0 :
                return -1 
            numdict[i] -= 1 
            numdict[score-i] -= 1

            chemistry += i * (score-i) 
        
        return chemistry
        