# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            curr = x 
            while curr != parent[curr]:
                curr = parent[curr]
            
            while x != curr:
                nx = parent[x]
                parent[x] = curr
                x = nx
            
            return curr
        
        def union(x, y):
            X, Y = find(x), find(y)
            if X != Y:
                parent[X] = Y
        
        parent = {i: i for i in range(1, len(edges)+1)}
        for x, y in edges:
            if find(x) == find(y):
                return [x, y]
            
            union(x, y)
    