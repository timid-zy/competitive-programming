class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        mod = pow(10, 9) + 7

        powers = [1]
        for i in range(1, len(nums)):
            powers.append((powers[-1] * 2) % mod)

        for i in range(len(nums)):
            r = bisect_right(nums, target - nums[i])
            if target - nums[i] < nums[0]: 
                break
        
            count = (count + powers[i]) % mod
            if r <= i:
                count -= powers[i - r]

        return count % mod