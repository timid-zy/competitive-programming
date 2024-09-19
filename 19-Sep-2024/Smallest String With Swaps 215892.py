# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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
            if X != Y:
                parent[X] = Y
        
        parent = {i: i for i in range(len(s))}
        for x, y in pairs:
            union(x, y)
        
        N = [i for i in range(len(s))]
        dct = defaultdict(list)
        for i in range(len(s)):
            N[i] = find(i)
            dct[find(i)].append(s[i])
        
        for k in dct:
            dct[k].sort(reverse=True)
        
        res = []
        for i in range(len(s)):
            res.append(dct[N[i]].pop())
        
        return "".join(res)
        