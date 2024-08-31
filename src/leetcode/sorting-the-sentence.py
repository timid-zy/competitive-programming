class Solution:
    def sortSentence(self, s: str) -> str:
        def getIdx(s): return int(s[-1])
        arr = s.split(" ")
        arr.sort(key=getIdx)

        ret_str = ""
        for i in range(len(arr)):
            ret_str += arr[i][:-1] + " "
        return ret_str[:-1]
