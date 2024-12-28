# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-v, k) for k, v in Counter(tasks).items()]
        heapify(heap)
        res = 0
        while heap:
            ls = []
            for _ in range(n+1):
                if not heap and not ls: break
                
                res += 1
                if not heap: continue
                
                c, k = heappop(heap)
                if c == -1: continue

                ls.append((c+1, k))

            for t in ls: heappush(heap, t)
            
        return res
