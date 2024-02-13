class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arrDict = {}
        for i in range(len(arr1)):
            if arr1[i] not in arrDict:
                arrDict[arr1[i]] = 1
            else:
                arrDict[arr1[i]] += 1
        retArr = []
        items_outside_arr2 = []
        for i in range(len(arr2)):
            if arr2[i] in arrDict:
                for j in range(arrDict[arr2[i]]):
                    retArr.append(arr2[i])
                arrDict[arr2[i]] = 0
        for key in arrDict:
            if arrDict[key] != 0:
                for i in range(arrDict[key]):
                    items_outside_arr2.append(key)
        items_outside_arr2.sort()
        return retArr + items_outside_arr2

        