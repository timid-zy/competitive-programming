class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        _sum = sum(nums)
        remainder = _sum % p
        if remainder == 0:
            return 0
        
        prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]
        
        min_len = len(nums)
        dict1 = {0: -1}
        for i in range(len(prefix)):
            curr_rem = prefix[i] % p
            complementary = (curr_rem - remainder) % p
            if complementary in dict1: 
                min_len = min(min_len, i - dict1[complementary])
            dict1[curr_rem] = i
        
        return min_len if min_len < len(nums) else -1
