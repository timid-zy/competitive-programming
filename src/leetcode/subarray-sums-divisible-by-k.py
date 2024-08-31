class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict1 = {0: 1}
        r_sum = 0
        count = 0
        
        for i in range(len(nums)):
            r_sum += nums[i]
            remainder = r_sum % k
            
            if remainder in dict1:
                count += dict1[remainder]
                dict1[remainder] += 1
            else: 
                dict1[remainder] = 1
        
        return count
