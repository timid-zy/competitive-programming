for _ in range(int(input())):
    n = input()
    person = []
    for i in range(int(n)):
        person.append(list(map(int, input().split())))
    
    person.sort(key=lambda x: x[1])
    
    arr = [p[0] for p in person]

    def mergeSort(arr):
        if len(arr) == 1:
            return arr
        
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

        return merge(left, right)


    def merge(left, right):
        global count
        # merge
        ans = []
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                ans.append(left[l])
                l += 1
            else:
                ans.append(right[r])
                count += len(left) - l
                r += 1
        
        ans.extend(left[l:])
        ans.extend(right[r:])

        return ans
        

    count = 0
    mergeSort(arr)
    print(count)