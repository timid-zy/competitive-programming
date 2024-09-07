# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
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
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        parent = {}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                for i in range(4):
                    parent[(r, c, i)] = (r, c, i)
        
        for ro in range(len(grid)):
            for c in range(len(grid[0])):
                t, r, b, l = [(ro, c, i) for i in range(4)]
                if inbound(ro, c-1):
                    union(t, (ro, c-1, 2))
                
                if inbound(ro-1, c):
                    union(l, (ro-1, c, 1))

                if grid[ro][c] == "/":
                    union(t, l); union(b, r)
                elif grid[ro][c] == "\\":
                    union(t, r); union(b, l)
                else:
                    union(t, r); union(r, b); union(b, l)

        parents = set()
        for k in parent: parents.add(find(k))
        return len(parents)
