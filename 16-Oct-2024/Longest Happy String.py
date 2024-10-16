class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = [(-a, "a"), (-b, "b"), (-c, "c")]
        for i in range(len(heap) - 1, -1, -1):
            if heap[i][0] == 0: heap.pop(i)

        heapify(heap)
        while len(heap) >= 2:
            count1, char1 = heappop(heap)
            count2, char2 = heappop(heap)

            if -count1 >= 2 and (not res or res[-1] != char1):
                res.extend([char1] * 2)
                count1 += 2
            else:
                res.append(char1)
                count1 += 1
            
            if -count2 >= 1:
                res.append(char2)
                count2 += 1

            if count1 != 0:
                heappush(heap, (count1, char1))
            if count2 != 0:
                heappush(heap, (count2, char2))

        if heap:
            count, char = heappop(heap)
            if not res or res[-1] != char:
                res.extend([char] * min(2, -count))
            elif len(res) == 1 or res[-2] != char:
                res.append(char)
        
        return "".join(res)
