class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        k = len(Counter(nums))
        count = 0
        curr = {}
        start = 0

        for i in range(len(nums)):
            curr[nums[i]] = curr.get(nums[i], 0) + 1
            
            while len(nums) > start and len(curr) == k:
                count += len(nums) - i
                curr[nums[start]] -= 1
                if curr[nums[start]] == 0:
                    del curr[nums[start]]
                start += 1
               
        
        return count
        