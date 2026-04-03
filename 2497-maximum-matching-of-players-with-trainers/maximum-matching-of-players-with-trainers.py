class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p = sorted(players)
        t = sorted(trainers)
        i = 0 
        count = 0

        for j in range(len(t)) :
            if i < len(p) and t[j] >= p[i] :
                i +=1 
                count += 1 
                
            if i == len(p):
                break

        return count

