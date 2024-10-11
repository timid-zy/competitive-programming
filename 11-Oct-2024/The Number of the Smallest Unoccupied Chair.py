class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr = list(zip(times, range(len(times))))
        arr.sort(key=lambda x: x[0][0])
        heap = []
        seats = []
        seat = 0
        for i in range(len(arr)):
            (arrival, leaving), idx = arr[i]
            while heap and heap[0][0] <= arrival:
                ol, os = heappop(heap)
                heappush(seats, os)
            
            if idx == targetFriend:
                return heappop(seats) if seats else seat
            
            if seats:
                heappush(heap, (leaving, heappop(seats)))
            else:
                heappush(heap, (leaving, seat))
                seat += 1
        