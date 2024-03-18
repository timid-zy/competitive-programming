class TimeMap:

    def __init__(self):
        self.values = {}
        self.stamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = [value]
            self.stamps[key] = [timestamp]
        else:
            self.values[key].append(value)
            self.stamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.stamps or self.stamps[key][0] > timestamp: return ""

        idx = bisect_right(self.stamps[key], timestamp)

        return self.values[key][idx - 1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)