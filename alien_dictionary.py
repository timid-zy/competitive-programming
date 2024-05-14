from collections import defaultdict, deque

class Solution:
    def findOrder(self, A, N, K):
        graph = defaultdict(list)
        indeg = defaultdict(int)

        for i in range(1, len(A)):
            p, c = A[i - 1], A[i]
            d = 0
            while d < len(p) and d < len(c):
                if p[d] != c[d]: break
                d += 1
            
            if d < len(p) and d < len(c):
                graph[p[d]].append(c[d])
                indeg[c[d]] += 1
        
        queue = deque()
        order = []
        for key in graph:
            if key not in indeg:
                queue.append(key)
                order.append(key)
        
        while queue:
            for _ in range(len(queue)):
                c = queue.popleft()
                for nb in graph[c]:
                    indeg[nb] -= 1
                    if indeg[nb] == 0:
                        queue.append(nb)
                        order.append(nb)
        
        for i in range(97, 97 + K):
            if chr(i) not in order:
                order.append(chr(i))
        
        return "".join(order)
