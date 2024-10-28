def shape(arr):
    for i in range(len(arr)):
        t = arr[i].split('-')
        arr[i] = (int(t[0]), t[1])
    
    return arr

def solve1(needle, haystack):
    res = 0
    for i in range(len(haystack)):
        if haystack[i][1] == needle[1]:
            res += max(0, haystack[i][0] - needle[0] + 1)

    return res

def solve2(needle, H):
    n1, n2 = needle
    res = 0
    for i in range(1, len(H)):
        if H[i][1] == n2[1] and H[i-1][1] == n1[1] and H[i-1][0] >= n1[0] and H[i][0] >= n2[0]:
            res += 1

    return res

def solveN(N, H):
    TN = N[1:-1]
    lps = [0] * len(TN)
    l, r = 0, 1
    while r < len(TN):
        if TN[l][1] == TN[r][1] and TN[l][0] == TN[r][0]:
            l += 1
            lps[r] = l
            r += 1
        elif l == 0:
            r += 1
        else:
            l = lps[l-1]
    
    res = 0
    ni = hi = 0
    while ni < len(TN) and hi < len(H):
        if TN[ni][1] == H[hi][1] and TN[ni][0] == H[hi][0]:
            ni += 1; hi += 1
        elif ni == 0:
            hi += 1
        else:
            ni = lps[ni-1]
    
        if ni == len(TN):
            hi -= 1
            st = hi - ni
            if st < 0 or hi+1 > len(H) - 1:
                continue
            
            if N[0][1] == H[st][1] and N[-1][1] == H[hi+1][1] and N[0][0] <= H[st][0] and N[-1][0] <= H[hi+1][0]:
                res += 1
            
            hi += 1

    return res

def solve():
    N, M = map(int, input().split())
    S1 = shape(input().split())
    S2 = shape(input().split())

    if M == 1:
        return solve1(S2[0], S1)
    elif M == 2:
        return solve2(S2, S1)
    
    return solveN(S2, S1)


print(solve())