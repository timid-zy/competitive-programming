# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = [False] * len(l)
        for i in range(len(l)):
            arr = sorted(nums[l[i]: r[i] + 1])
            if len(arr) <= 1:
                continue
            
            d = arr[1] - arr[0]
            invalid = False
            for j in range(2, len(arr)):
                if arr[j] - arr[j-1] != d:
                    invalid = True
                    break
            
            if invalid:
                continue
            
            ans[i] = True
    
        return ans
