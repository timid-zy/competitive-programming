class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        curr_odds = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                if curr_odds < k - 1:
                    curr_odds += 1
                    continue
                
                evens_before = 0
                while nums[start] % 2 == 0:
                    evens_before += 1
                    start += 1
                start += 1
                
                evens_after = 0
                next_ = end + 1
                while next_ < len(nums) and nums[next_] % 2 == 0:
                    evens_after += 1
                    next_ += 1
                
                count += (evens_before + 1) * (evens_after + 1)

        return count