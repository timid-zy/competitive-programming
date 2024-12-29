# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        curr = mx = 0
        res = [0]
        for i, x in enumerate(nums):
            if nums[i] == 1:
                curr -= 1
                continue

            curr += 1
            if curr > mx:
                res = [i+1]
                mx = curr
            elif curr == mx:
                res.append(i+1)
            
        return res