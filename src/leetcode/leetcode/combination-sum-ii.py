class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        arr = []
        candidates.sort()
        def combos(currArr, currSum, idx):
            nonlocal arr
            if currSum > target:
                return
            
            if currSum == target:
                arr.append(tuple(currArr))
                return
            
            visited = set()
            for i in range(idx, len(candidates)):
                if candidates[i] not in visited:
                    combos(currArr + [candidates[i]], currSum + candidates[i], i + 1)
                    visited.add(candidates[i])
            
        combos([], 0, 0)
        return arr