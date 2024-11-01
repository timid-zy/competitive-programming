# Problem: Longest Increasing Subsequence II - https://leetcode.com/problems/longest-increasing-subsequence-ii/description/

class SegmentTree:

    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * self.n)        
       
        
    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2*index], self.tree[2*index + 1])
        
    def range_max(self, left, right):
        left += self.n
        right += self.n + 1
        res = 0
        while left < right:
            if left % 2 == 1:
                res = max(res, self.tree[left])
                left += 1
            
            if right % 2 == 1:
                right -= 1
                res = max(res, self.tree[right])
            
            left //= 2
            right //= 2
        
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        seg = SegmentTree(max(nums) + 1)
        for n in nums:
            ls = seg.range_max(max(1, n-k), n-1) + 1
            seg.update(n, ls)
        
        return max(seg.tree)