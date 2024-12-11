class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # prefix = [0] * (max(nums) + k + 1)
        # for n in nums:
        #     prefix[n+k] += 1
        #     if n-k-1 >= 1:
        #         prefix[n-k-1] -= 1
            
        # for i in range(len(prefix) - 2, -1, -1):
        #     prefix[i] += prefix[i+1]
        
        # return max(prefix[1:])

        nums.sort()
        l = res = 0
        for r in range(len(nums)):
            while l < r and nums[r] - nums[l] > 2*k:
                l += 1
            
            res = max(res, r-l+1)

        return res