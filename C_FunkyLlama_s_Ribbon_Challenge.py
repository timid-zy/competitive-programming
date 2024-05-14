
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    arr = list(map(int, input().split()))
    N = arr[0]

    def dp(r):
        if r < 0:
            return float('-inf')
    
        if r == 0:
            return 0
        
        if r in memo:
            return memo[r]
        
        memo[r] = max(
            dp(r - arr[1]) + 1,
            dp(r - arr[2]) + 1,
            dp(r - arr[3]) + 1,
        )
        
        return memo[r]

    memo = {}
    print(dp(N))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
