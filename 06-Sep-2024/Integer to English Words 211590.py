# Problem: Integer to English Words - https://leetcode.com/problems/integer-to-english-words/

class Solution:
    SINGLE = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    TENS = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}
    TEENS = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    PLACES = {0: "", 1: "Thousand", 2: "Million", 3: "Billion"}

    def convert_segment(self, s):
        s = s.lstrip("0")
        if s == "":
            return ""
        
        n = int(s)
        if n <= 9:
            return self.SINGLE[n]
        elif n <= 19:
            return self.TEENS[n]
        elif n <= 99:
            sc = " " + self.SINGLE[int(s[1])] if int(s[1]) != 0 else ""
            return f"{self.TENS[int(s[0])]}{sc}"

        nxt = self.convert_segment(s[1:])
        suf = " " + nxt if nxt != "" else ""
        return f"{self.SINGLE[int(s[0])]} Hundred{suf}"

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        segs = []; s = str(num)[::-1]
        for i in range(0, len(s), 3):
            segs.append(s[i:i+3])
        
        res = ""
        for i in range(len(segs) - 1, -1, -1):
            seg = segs[i][::-1]
            conv = self.convert_segment(seg)
            if conv.strip() != "":
                res += f"{conv} {self.PLACES[i]} "

        return res.rstrip()
