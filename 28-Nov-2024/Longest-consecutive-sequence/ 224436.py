# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(x):
            curr = x
            while curr != parent[curr]:
                curr = parent[curr]
            
            while x != parent[x]:
                nx = parent[x]
                parent[x] = curr
                x = nx
            
            return curr

        def union(x, y):
            X, Y = find(x), find(y)
            parent[X] = Y
            
        parent = {}
        for n in nums:
            parent[n] = n

        for n in nums:
            if n-1 in parent:
                union(n-1, n)
            if n+1 in parent:
                union(n, n+1)
        
        len_counter = defaultdict(int)
        res = 0
        for n in parent:
            p = find(n)
            len_counter[p] += 1
            res = max(res, len_counter[p])

        return res
