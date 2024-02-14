class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        hand.sort()
        for i in range(len(hand)):
            if hand[i] in count: count[hand[i]] += 1
            else: count[hand[i]] = 1

        for i in range(len(hand)):
            curr = hand[i]
            if count[hand[i]] <= 0:
                continue
    
            for j in range(groupSize):
                if curr + j not in count or count[curr + j] <= 0:
                    return False
                count[curr + j] -= 1

        return True
            