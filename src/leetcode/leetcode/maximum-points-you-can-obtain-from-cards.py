class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        sum_all = sum(cardPoints)
        window_size = len(cardPoints) - k
        window_sum = sum(cardPoints[:window_size])
        min_sum = window_sum
        for start in range(1, len(cardPoints) - window_size + 1):
            window_sum -= cardPoints[start - 1]
            window_sum += cardPoints[start + window_size - 1]
            min_sum = min(min_sum, window_sum)
        
        return sum_all - min_sum
