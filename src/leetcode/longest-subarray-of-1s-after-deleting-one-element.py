class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len = 0
        start = 0
        deleted = False
        zero_idx = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                if deleted:
                    start = zero_idx + 1
                else:
                    deleted = True
                zero_idx = end
            # print(start, end, zero_idx)
            max_len = max(max_len, end - start)
        
        return max_len