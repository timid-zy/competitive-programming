class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        ans = defaultdict(int)
        res = float('-inf')
        for n in nums:
            ans[n] = 1 + ans[n**0.5] 
            res = max(res, ans[n])
        
        return res if res >= 2 else -1