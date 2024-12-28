# Problem: Maximum Sum of 3 Non-Overlapping Subarrays - https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        mx = cs = sum(nums[:k])
        mxi = 0
        prefix = [(mxi, cs)]
        for i in range(1, len(nums)-k+1):
            cs += nums[i+k-1] - nums[i-1]
            if cs > mx:
                mx = cs
                mxi = i

            prefix.append((mxi, mx))
        
        mx = cs = sum(nums[-k:])
        mxi = len(nums)-k
        suffix = [(mxi, cs)]
        for i in range(len(nums)-k-1, -1, -1):
            cs += nums[i] - nums[i+k]
            if cs >= mx:
                mx = cs
                mxi = i
            
            suffix.append((mxi, mx))
        
        suffix = suffix[::-1]
        cs = sum(nums[k-1:k+k-1])
        mx = float('-inf')
        res = [0, 0, 0]
        for i in range(k, len(nums)-k-k+1):
            p = i-k
            s = i+k
            cs += nums[i+k-1] - nums[i-1]
            if prefix[p][1] + suffix[s][1] + cs > mx:
                mx = prefix[p][1] + suffix[s][1] + cs
                res = [prefix[p][0], i, suffix[s][0]]
            
        return res