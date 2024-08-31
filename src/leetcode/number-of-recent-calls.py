class RecentCounter:

    def __init__(self):
        self.pings = []
        self.count = 0
        
    def ping(self, t: int) -> int:
        self.pings.append(t)
        for i in range(self.count, len(self.pings)):
            if self.pings[i] >= t - 3000:
                self.count = i
                return len(self.pings) - i
        return 0
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t