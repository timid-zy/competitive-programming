class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = []

        def findCombinations(currArr, start=1):
            if len(currArr) == k:
                arr.append(currArr)
                return
            
            for i in range(start, n + 1):
                currArr.append(i)
                findCombinations(currArr[:], i + 1)
                currArr.pop()
        
        findCombinations([])
        return arr
