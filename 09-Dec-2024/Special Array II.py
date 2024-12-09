class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        mis = [0] * len(nums)
        for i in range(1, len(nums)):
            mis[i] = mis[i-1]
            if nums[i] % 2 == nums[i-1] % 2:
                mis[i] += 1
                

        res = []
        for ql, qr in queries:
            res.append(mis[ql] == mis[qr])
        
        return res