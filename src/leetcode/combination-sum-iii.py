class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        combos = []
        def backtrack(currArr, currSum, count, last):
            if currSum == n and count == 0:
                combos.append(currArr)
                return
            
            if currSum > n: return
            
            for i in range(last, 10):
                backtrack(currArr + [i], currSum + i, count - 1, i + 1)
        
        backtrack([], 0, k, 1)
        return combos