class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible(div):
            sum_ = 0
            for i in range(len(nums)):
                sum_ += math.ceil(nums[i] / div)
            return sum_ <= threshold

        l, r = 1, max(nums)
        while l < r:
            mid = l + (r - l) // 2
            if not possible(mid):
                l = mid + 1 
            else:
                r = mid
            
        return r