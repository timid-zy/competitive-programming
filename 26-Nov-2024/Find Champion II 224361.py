# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for u, v in edges:
            indegree[v] += 1
        
        champ = None
        for node in range(n):
            if indegree[node] == 0 and champ is None:
                champ = node
            elif indegree[node] == 0:
                return -1
        
        return champ