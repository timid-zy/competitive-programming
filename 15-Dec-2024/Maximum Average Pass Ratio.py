class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for p, t in classes:
            heappush(heap, ((p/t) - ((p+1)/(t+1)), p, t))
        
        for _ in range(extraStudents):
            __, po, to = heappop(heap)
            po += 1
            to += 1
            heappush(heap, (po/to - ((po+1)/(to+1)), po, to))
        
        sm = 0
        for h, p, t in heap:
            sm += p/t
        
        return sm / len(heap)
    