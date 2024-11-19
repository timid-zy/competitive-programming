# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        sm = 0
        for i in range(k):
            counter[nums[i]] += 1
            sm += nums[i]

        res = 0
        for i in range(len(nums)-k+1):
            if i > 0:
                counter[nums[i-1]] -= 1
                if counter[nums[i-1]] == 0:
                    del counter[nums[i-1]]

                counter[nums[i+k-1]] += 1
                sm -= nums[i-1]
                sm += nums[i+k-1]

            if len(counter) == k:
                res = max(res, sm)
            
        return res

