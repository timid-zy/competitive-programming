class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        ans = deque()
        ans.append(deck[0])
        for i in range(1, len(deck)):
            num = ans.pop()
            ans.appendleft(num)
            ans.appendleft(deck[i])
        
        return list(ans)