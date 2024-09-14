# Problem: Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        def traverse(i, graph, visited):
            queue = deque([i])
            visited.add(i)
            res = [i]
            while queue:
                c = queue.popleft()
                for nb in graph[c]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
                        res.append(nb)
                
            return res

        graph = defaultdict(list)
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        
        components = []
        visited = set()
        for i in range(len(source)):
            if i not in visited:
                components.append(traverse(i, graph, visited))
    
        diff = 0
        for comp in components:
            counter = defaultdict(int)
            for idx in comp:
                counter[source[idx]] += 1
            
            for idx in comp:
                if counter[target[idx]] > 0:
                    counter[target[idx]] -= 1
                else:
                    diff += 1
        
        return diff