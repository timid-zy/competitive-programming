class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}; i = 1
        for n in sorted(set(arr)):
            ranks[n] = i; i += 1
        
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        
        return arr