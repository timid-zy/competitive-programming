# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n2 = 0
        for x in nums2: n2 ^= x

        res = 0
        for x in nums1: 
            res ^= n2
            if len(nums2) % 2 == 1:
                res ^= x
            
        return res