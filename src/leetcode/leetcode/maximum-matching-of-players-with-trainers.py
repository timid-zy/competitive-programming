class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        p1 = 0
        t1 = 0
        pairs = 0
        
        while p1 < len(players) and t1 < len(trainers):
            if players[p1] <= trainers[t1]:
                pairs += 1
                t1 += 1
                p1 += 1
                
            else:
                t1 += 1
        
        return pairs