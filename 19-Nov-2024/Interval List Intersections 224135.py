# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, F: List[List[int]], S: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        while i < len(F) and j < len(S):
            l1, r1 = F[i]
            l2, r2 = S[j]

            if l2 <= l1 <= r2 or l1 <= l2 <= r1 or (l1 <= l2 and r2 <= r1) or (l2 <= l1 and r1 <= r2):
                res.append([max(l1, l2), min(r1, r2)])
            
            if r1 > r2:
                j += 1
            else:
                i += 1
            
        return res
    