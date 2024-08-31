class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        curr_len = 0
        zeroes = 0
        max_len = 0
        start = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                curr_len += 1
            else:
                zeroes += 1
                while zeroes > k:
                    if nums[start] == 0:
                        zeroes -= 1
                    start += 1
            max_len = max(max_len, end - start + 1)
        
        return max_len
                