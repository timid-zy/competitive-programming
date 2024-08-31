class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        left = 0
        white_no = blocks[:k].count('W')
        min_white = white_no

        while left < len(blocks) - k:
            left += 1
            if blocks[left - 1] == "W":
                white_no -= 1
            if blocks[left + k - 1] == "W":
                white_no += 1
            
            min_white = min(min_white, white_no)
        
        return min_white
