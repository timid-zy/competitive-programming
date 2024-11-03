# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.arr = []
        

    def book(self, start: int, end: int) -> bool:
        for x, y in self.arr:
            if x <= start < y or x < end <= y or (start <= x and y <= end):
                return False

        self.arr.append((start, end))
        return True      


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)