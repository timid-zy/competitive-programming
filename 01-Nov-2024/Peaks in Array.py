class SegmentTree:

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        self.nums = nums

        self.build()
    
    def check_peak(self, index):
        if index == 0 or index == self.n - 1:
            return 0
        
        return 1 if self.nums[index-1] < self.nums[index] and self.nums[index] > self.nums[index+1] else 0
    
    def build(self):
        for i in range(self.n):
            self.tree[i+self.n] = self.check_peak(i)   
        
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]
    
    def update_helper(self, index):
        index += self.n
        index //= 2
        while index >= 1:
            self.tree[index] = self.tree[2*index] + self.tree[2*index + 1]
            index //= 2
    
    def update(self, index, value):
        self.nums[index] = value
        if index - 1 > 0:
            self.tree[index - 1 + self.n] = self.check_peak(index-1)
            self.update_helper(index - 1)
        
        if index + 1 < self.n - 1:
            self.tree[index + 1 + self.n] = self.check_peak(index+1)
            self.update_helper(index + 1)
        
        self.tree[index + self.n] = self.check_peak(index)
        self.update_helper(index)
    
    def range_sum(self, left, right):
        left += self.n
        right += self.n + 1
        res = 0
        while left < right:
            if left % 2 == 1:
                res += self.tree[left]
                left += 1

            if right % 2 == 1:
                right -= 1
                res += self.tree[right]
            
            left //= 2
            right //= 2
        
        return res

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        seg = SegmentTree(nums)
        res = []
        for op, l, r in queries:
            if op == 1:
                res.append(seg.range_sum(l+1, r-1))
            else:
                seg.update(l, r)
        
        return res
