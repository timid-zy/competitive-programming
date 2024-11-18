# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(l, r, arr):
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            
        res = []
        for i in range(len(arr) - 1, -1, -1):
            mxi = i
            for j in range(i):
                if arr[j] > arr[mxi]:
                    mxi = j
            
            if mxi == i:
                continue
            
            if mxi != 0:
                res.append(mxi + 1)
            
            res.append(i + 1)
            reverse(0, mxi, arr)
            reverse(0, i, arr)
        
        return res
            
