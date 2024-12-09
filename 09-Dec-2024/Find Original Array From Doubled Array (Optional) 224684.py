# Problem: Find Original Array From Doubled Array (Optional) - https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        count = Counter(changed)
        mp = []
        changed.sort()
        for n in changed:
            if count[n] == 0:
                continue
            
            if count[n*2] > 0:
                count[n*2] -= 1
                count[n] -= 1
                mp.append(n)
            else:
                return []
        
        return mp