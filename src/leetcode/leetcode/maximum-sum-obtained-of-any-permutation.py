class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # 3:05 - 3:21
        range_prefix = [0] * (len(nums) + 1)

        for start, end in requests:
            range_prefix[start] += 1
            range_prefix[end + 1] -= 1

        # compute the prefix sum
        for i in range(1, len(range_prefix)):
            range_prefix[i] += range_prefix[i - 1]
        
        nums.sort()
        range_prefix.sort()
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i] * range_prefix[i + 1]

        return sum1 % (pow(10, 9) + 7)