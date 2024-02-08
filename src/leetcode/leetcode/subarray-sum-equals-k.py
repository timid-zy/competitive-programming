class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = {0 : 1}
        r_sum = 0
        count = 0
        for i in range(len(nums)):
            r_sum += nums[i]
            diff = r_sum - k
            if diff in dict1:
                count += dict1[diff]
            
            if r_sum in dict1:
                dict1[r_sum] += 1
            else:
                dict1[r_sum] = 1
        
        return count