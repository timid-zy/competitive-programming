class Solution:
    def smallestNumber(self, num: int) -> int:
        strNum = list(str(num))
        ans = ""
        if num > 0:
            strNum = sorted(strNum)
            for i in range(len(strNum)):
                if strNum[i] != "0":
                    ans = strNum[i]
                    strNum.pop(i)
                    break
        elif num < 0:
            strNum = sorted(strNum, reverse=True)[:-1]

        for i in range(len(strNum)):
                ans += strNum[i]
        return int(ans) if num > 0 else -1 * int(ans)