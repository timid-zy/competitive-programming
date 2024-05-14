import sys, threading
from collections import Counter

input = lambda: sys.stdin.readline().strip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = Counter(A)
    arr = sorted(list(set(A)))
    memo = {}
    
    def dp(i, last):
        if i >= len(arr):
            return 0
        
        if arr[i] == last + 1:
            return dp(i + 1, last)

        if i in memo:
            return memo[i]
        
        memo[i] = max(
            dp(i + 1, arr[i]) + (arr[i] * counter[arr[i]]),
            dp(i + 1, last)
        )

        return memo[i]

    print(dp(0, -1))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
