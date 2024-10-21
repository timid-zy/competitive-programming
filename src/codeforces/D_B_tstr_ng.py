def solve():
    N, K = map(int, input().split())
    S = list(input())
    arr = [""] * K

    for i, c in enumerate(S):
        if c == "?":
            continue
        
        if arr[i%K] != "" and arr[i%K] != c:
            return "NO"

        arr[i%K] = c
    
    
    return "YES" if abs(arr.count("1") - arr.count("0")) - arr.count("") <= 0 else "NO"


for _ in range(int(input())):
    print(solve())