# Problem: Sum of Distances in Tree - https://leetcode.com/problems/sum-of-distances-in-tree

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def traverse(node, parent):
            score, count = 0, 1
            for nb in graph[node]:
                if nb != parent:
                    sc, co = traverse(nb, node)
                    score, count = score + sc + co, count + co
            
            dp[node] = count
            return score, count
        
        def solve(node, parent):
            if parent != -1:
                dp[node] = dp[parent] - 2*dp[node] + n

            for nb in graph[node]:
                if nb != parent: solve(nb, node)
       
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        dp = [0] * n
        total_score, _ = traverse(0, -1)
        dp[0] = total_score
        solve(0, -1)

        return dp
