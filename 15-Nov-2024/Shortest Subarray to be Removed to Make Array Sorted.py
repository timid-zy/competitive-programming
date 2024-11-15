class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        r = len(arr) - 1
        while r > 0 and arr[r] >= arr[r-1]:
            r -= 1
        
        if r == 0:
            return 0
        
        l = 0
        res = r
        while l < len(arr):
            if (l > 0 and arr[l] < arr[l-1]):
                break
            
            while r < len(arr) and arr[l] > arr[r]:
                r += 1
            
            res = min(res, r-l-1)
            l += 1
        
        return res
            
