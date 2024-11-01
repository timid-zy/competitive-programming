# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, G: List[List[int]]) -> bool:
        rect = {} # rmn, rmx, cmn, cmx
        for r in range(len(G)):
            for c in range(len(G[0])):
                color = G[r][c]
                if color not in rect:
                    rect[color] = [r, r, c, c]
                
                rmn, rmx, cmn, cmx = rect[color]
                rect[color] = [min(rmn, r), max(rmx, r), min(cmn, c), max(cmx, c)]
        
        graph = defaultdict(set)
        for color in rect:
            rmn, rmx, cmn, cmx = rect[color]
            for r in range(rmn, rmx+1):
                for c in range(cmn, cmx+1):
                    if G[r][c] != color:
                        graph[color].add(G[r][c])

        indeg = defaultdict(int)
        for k in rect:
            for child in graph[k]:
                indeg[child] += 1
        
        queue = deque()
        for k in rect:
            if indeg[k] == 0:
                queue.append(k)
        
        seen = set()
        while queue:
            n = queue.popleft()
            seen.add(n)
            for nb in graph[n]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    queue.append(nb)

        return len(seen) == len(rect.keys())
