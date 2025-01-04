# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(st):
            stk = [st]
            seen = set([st])
            while stk:
                cur = stk.pop()
                for nb in graph[cur]:
                    if nb not in seen:
                        seen.add(nb)
                        stk.append(nb)
            
            return len(seen)

                
        graph = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                    if (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2 <= bombs[i][2] ** 2:
                        graph[i].append(j)
        
        return max(dfs(st) for st in range(len(bombs)))