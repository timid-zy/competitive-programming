class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # 2:12 - 2:2
        prefix = [0] * (n + 2)

        for first, last, seats in bookings:
            prefix[first] += seats
            prefix[last + 1] -= seats
        
        # compute the prefix sum
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        return prefix[1: -1]