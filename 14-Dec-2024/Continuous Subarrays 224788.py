# Problem: Continuous Subarrays - https://leetcode.com/problems/continuous-subarrays/

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = res = 0
        count = defaultdict(int)
        for r in range(len(nums)):
            rs = sum(count[n] for n in range(nums[r]-2, nums[r]+3))
            while l < r and rs != r-l:
                if abs(nums[r] - nums[l]) <= 2:
                    rs -= 1
                    
                count[nums[l]] -= 1
                l += 1
            
            count[nums[r]] += 1
            res += r-l+1
        
        return res