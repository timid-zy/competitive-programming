class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n_num = [0] * (len(customers))
        y_num = [0] * (len(customers))
        n_num[0] = 1 if customers[0] == "N" else 0
        y_num[-1] = 1 if customers[-1] == "Y" else 0

        for i in range(1, len(customers)):
            if customers[i] == "N":
                n_num[i] = n_num[i - 1] + 1
            else:
                n_num[i] = n_num[i - 1]
        
        for i in range(len(customers) - 2, -1, -1):
            if customers[i] == "Y":
                y_num[i] = y_num[i + 1] + 1
            else:
                y_num[i] = y_num[i + 1]
        
        y_num.append(0)
        n_num.insert(0, 0)
        
        min_hour = y_num[0] + n_num[0]
        min_hour_idx = 0
        for i in range(1, len(n_num)):
            if min_hour > y_num[i] + n_num[i]:
                min_hour_idx = i
                min_hour = y_num[i] + n_num[i]
        
        return min_hour_idx