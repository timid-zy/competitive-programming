# Problem: My Calendar II - https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:

    def __init__(self):
        self.singles = []
        self.doubles = []

    def book(self, start: int, end: int) -> bool:
        end -= 1
        for x, y in self.doubles:
            if x <= start <= y or x <= end <= y or (start < x and y < end):
                return False
        
        for x, y in self.singles:
            if x <= start <= y or x <= end <= y or (start < x and y < end):
                self.doubles.append((max(x, start), min(y, end)))
        
        self.singles.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)