# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def check_hIndex(h, cit):
            c = 0
            for candh in cit:
                if candh >= h:
                    c += 1
            
            return c >= h


        l, r = 0, max(citations)
        while l < r:
            mid = (r + l + 1) // 2
            if check_hIndex(mid, citations):
                l = mid
            else:
                r = mid - 1
        
        return l