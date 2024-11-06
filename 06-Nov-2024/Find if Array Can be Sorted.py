class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        pb = None
        psm = float('-inf')
        csm = float('-inf')
        for n in nums:
            if pb == n.bit_count():
                if psm > n: return False
                csm = max(n, csm)
                continue

            if csm > n:
                return False
            
            pb = n.bit_count()
            psm = csm
            csm = n
                
        return True