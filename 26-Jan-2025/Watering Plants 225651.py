# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        c = capacity
        res = 0
        for i in range(len(plants)):
            if plants[i] <= c:
                res += 1
                c -= plants[i]
            else:
                res += 2*i + 1
                c = capacity - plants[i]
        
        return res