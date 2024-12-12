class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-n for n in gifts]
        heapify(heap)
        for _ in range(k):
            mx = -heappop(heap)
            heappush(heap, -1 * int(mx ** 0.5))

        return -sum(heap)