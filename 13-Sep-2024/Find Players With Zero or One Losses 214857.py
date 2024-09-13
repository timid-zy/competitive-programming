# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        nl, ol, mr = set(), set(), set()
        for x, y in matches:
            if x not in ol and x not in mr:
                nl.add(x)

            if y not in mr and y not in ol:
                nl.discard(y); ol.add(y)
            elif y in ol:
                ol.remove(y); mr.add(y)
        
        return [sorted(list(nl)), sorted(list(ol))]