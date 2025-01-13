# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indeg[x] += 1
            indeg[y] += 1
        
        queue = deque()
        for i in range(n):
            if indeg[i] <= 1:
                queue.append(i)
        
        while n > 2:
            n -= len(queue)
            for _ in range(len(queue)):
                curr = queue.popleft()
                for nb in graph[curr]:
                    indeg[nb] -= 1
                    if indeg[nb] == 1:
                        queue.append(nb)

        return list(queue)