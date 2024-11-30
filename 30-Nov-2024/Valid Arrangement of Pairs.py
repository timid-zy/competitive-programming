class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indeg = defaultdict(int)
        for a, b in pairs:
            graph[a].append(b)
            indeg[a] += 1
            indeg[b] -= 1
    
        start = pairs[0][0]
        for k in indeg:
            if indeg[k] == 1:
                start = k
                break
        
        path = []
        stk = [start]
        while stk:
            while graph[stk[-1]]:
                last = graph[stk[-1]].pop()
                stk.append(last)
            
            path.append(stk.pop())
        
        # print(path)
        res = []
        for i in range(len(path)-2, -1, -1):
            res.append([path[i+1], path[i]])

        return res
