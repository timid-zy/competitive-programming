# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        none, ones, more = set(), set(), set()
        for w, l in matches:
            if w not in ones and w not in more:
                none.add(w)
            
            none.discard(l)
            if l not in ones and l not in more:
                ones.add(l)
            elif l in ones:
                ones.remove(l)
                more.add(l)
        
        return [sorted(list(none)), sorted(list(ones))]
