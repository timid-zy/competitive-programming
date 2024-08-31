class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        r_sum = 0
        num = tickets[k]
        count = 0
        count_to_right = 0

        for i in range(len(tickets)):
            if tickets[i] >= num:
                count += 1
                if i > k:
                    count_to_right += 1
            else:
                r_sum += tickets[i]
        
        return (count * num + r_sum) - (count_to_right)