class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        pos = [0] * 33
        for n in candidates:
            for i in range(33):
                if n & (1 << i):
                    pos[i] += 1
        
        return max(pos)