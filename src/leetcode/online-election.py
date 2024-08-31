class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        dict1 = {}
        max_ = None
        self.data = []
        for i in range(len(persons)):
            dict1[persons[i]] = dict1.get(persons[i], 0) + 1
            if max_ not in dict1 or dict1[max_] <= dict1[persons[i]]:
                max_ = persons[i]
            self.data.append(max_)
        self.time = times

    def q(self, t: int) -> int:
        idx = bisect_left(self.time, t)
        
        if idx < len(self.time) and self.time[idx] == t:
            return self.data[idx]
        return self.data[idx - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)