class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        dict1 = {}
        start = 0
        min_ = len(cards) + 1

        for end in range(len(cards)):
            num = cards[end]
            if num in dict1 and dict1[num] >= start:
                min_ = min(min_, end - dict1[num] + 1) 
                start = dict1[num] + 1

            dict1[num] = end
        
        return min_ if min_ != len(cards) + 1 else -1