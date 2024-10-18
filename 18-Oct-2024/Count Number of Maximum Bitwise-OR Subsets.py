class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def backtrack(i, res):
            nonlocal count, mx            
            if i == len(nums):
                return
            
            if res | nums[i] == mx:
                count += 1
            
            backtrack(i+1, res)
            backtrack(i+1, res | nums[i])

        count = mx = 0
        for n in nums:
            mx |= n

        backtrack(0, 0)
        return count
