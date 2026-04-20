class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        asteroids.sort()
        for i in asteroids:
            if (mass > 0) and (i <= mass) :
                mass += i 
            else : 
                return False
        return True
        