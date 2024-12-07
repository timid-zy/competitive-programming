class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def check_val(res):
            ops = 0
            for i in range(len(nums)):
                if nums[i] > res:
                    ops += (nums[i]) // res
                    if nums[i] % res == 0: ops -= 1
            
            return ops <= maxOperations
        
        l, r = 1, max(nums)
        while l < r:
            mid = l + (r-l) // 2
            if check_val(mid):
                r = mid
            else:
                l = mid + 1
        
        return l