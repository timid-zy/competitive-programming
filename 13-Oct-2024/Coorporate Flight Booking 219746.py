# Problem: Coorporate Flight Booking - https://leetcode.com/problems/corporate-flight-bookings/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * (n + 1)
        for f, l, s in bookings:
            seats[f-1] -= s
            seats[l] += s
        
        for i in range(len(seats) - 2, -1, -1):
            seats[i] += seats[i+1]
        
        return seats[1:]