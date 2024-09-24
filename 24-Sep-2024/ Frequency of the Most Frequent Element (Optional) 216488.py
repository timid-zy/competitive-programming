# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        def get_range_sum(l, r, prefix):
            if l == 0:
                return prefix[r]
            
            return prefix[r] - prefix[l-1]


        def binary_search(l, r, prefix):
            li, ri = l, r
            while l < r:
                mid = l + (r - l) // 2
                if (ri-mid+1)*nums[ri+1] - get_range_sum(mid, ri, prefix) <= k:
                    r = mid
                else:
                    l = mid + 1

            return l


        nums.sort()
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        res = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > k:
                continue

            res = max(
                res,
                i - binary_search(0, i-1, prefix) + 1
            )

        return res
    