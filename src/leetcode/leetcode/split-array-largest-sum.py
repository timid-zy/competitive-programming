class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checkMax(mx):
            segs = 1
            r_sum = 0
            for i in range(len(nums)):
                r_sum += nums[i]
                if r_sum > mx:
                    segs += 1
                    r_sum = nums[i]


            return segs <= k

        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + (r - l) // 2
            if checkMax(mid):
                r = mid
            else: 
                l = mid + 1
        
        return l