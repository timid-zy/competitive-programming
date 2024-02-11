class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        dict1 = {0: 1}
        r_sum = 0
        count = 0
        for i in range(len(nums)):
            r_sum += nums[i]
            target = r_sum - goal

            if target in dict1:
                count += dict1[target]
            
            if r_sum not in dict1:
                dict1[r_sum] = 1
            else: 
                dict1[r_sum] += 1
        return count