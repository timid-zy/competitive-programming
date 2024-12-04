# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def find(x, parent):
            curr = x
            while curr != parent[curr]:
                curr = parent[curr]
            
            while x != parent[x]:
                nx = parent[x]
                parent[x] = curr
                x = nx
            
            return parent[x]
        
        def union(x, y, parent):
            X, Y = find(x, parent), find(y, parent)
            if X != Y:
                parent[Y] = X

        meetings.sort(key=lambda meeting: meeting[2])
        parents = {}
        res = set([0, firstPerson])
        prev_time = 0
        for p1, p2, time in meetings:
            if time != prev_time:
                sp = set()
                for k in parents:
                    if k in res: sp.add(find(k, parents))

                for k in parents:
                    if find(k, parents) in sp:
                        res.add(k)
                
                parents = {}

            prev_time = time
            if p1 not in parents:
                parents[p1] = p1
            
            if p2 not in parents:
                parents[p2] = p2
            
            union(p1, p2, parents)
        
        sp = set()
        for k in parents:
            if k in res: sp.add(find(k, parents))

        for k in parents:
            if find(k, parents) in sp:
                res.add(k)
        
        return list(res)