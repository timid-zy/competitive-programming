def getRangeSum(prefix, l, r):
    if l == 0:
        return prefix[r]

    return prefix[r] - prefix[l - 1]


for i in range(int(input())):
    input()
    arr = list(map(int, input().split()))

    ans = ""
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])

    
    for _ in range(int(input())):
        l, u = list(map(int, input().split()))
        l -= 1
        st = l
        r = len(arr) - 1

        while l < r:
            mid = l + (r - l) // 2
            r_sum = getRangeSum(prefix, st, mid)
            res = ((2 * u - (r_sum - 1)) * r_sum) // 2
            
            if mid < len(arr) - 1:
                nr_sum = r_sum + arr[mid + 1]
                nxt = ((2 * u - (nr_sum - 1)) * nr_sum) // 2

                if res < nxt:
                    l = mid + 1
                else:
                    r = mid
            
            else:
                pr_sum = r_sum - arr[mid]
                prev = ((2 * u - (pr_sum - 1)) * pr_sum) // 2

                if prev < res:
                    l = r = mid
                else:
                    l = r = mid - 1
                

        ans += str(l + 1) + " "
    
    print(ans)