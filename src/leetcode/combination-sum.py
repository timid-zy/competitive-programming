class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(arr, currSum=0, idx=0):
            if currSum == target:
                combinations.append(arr)
                return
            
            for i in range(idx, len(candidates)):
                if currSum < target:
                    backtrack(arr + [candidates[i]], currSum + candidates[i], i)
        
        combinations = []
        backtrack([])
        return combinations