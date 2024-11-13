# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def get_left(l, val, nums):
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < val:
                    l = mid + 1
                else:
                    r = mid
            
            return l
        
        def get_right(l, val, nums):
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= val:
                    l = mid + 1
                else:
                    r = mid
            
            return r

        nums.sort()
        res = 0
        for i, n in enumerate(nums):
            l = get_left(i+1, lower - n, nums)
            r = get_right(i+1, upper - n, nums)
            res += max(0, r-l)
        
        return res