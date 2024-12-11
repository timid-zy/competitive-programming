# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.averages = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_location, start_time = self.customers[id]
        new_val = t - start_time
        key = (start_location, stationName)
        if key not in self.averages:
            self.averages[key] = (new_val, 1)
            return
        
        old_av, old_c = self.averages[key]
        new_av = (old_av * old_c + new_val) / (old_c + 1)
        self.averages[key] = (new_av, old_c + 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averages[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)