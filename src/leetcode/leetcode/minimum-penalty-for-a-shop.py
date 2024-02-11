class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_hour = -1 # 0th hour
        curr_Y = 0
        max_Y = 0

        for i in range(len(customers)):
            if customers[i] == "Y":
                curr_Y += 1
            else:
                curr_Y -= 1
            
            if max_Y < curr_Y:
                max_Y = curr_Y
                max_hour = i
        
        return max_hour + 1