# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, N: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for x, y in prerequisites:
            graph[y].append(x)
            indeg[x] += 1
        
        queue = deque()
        visited = set()
        for i in range(N):
            if indeg[i] == 0:
                visited.add(i)
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            for nb in graph[curr]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    visited.add(nb)
                    queue.append(nb)
        
        return len(visited) == N