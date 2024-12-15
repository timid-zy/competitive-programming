import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def solve():
        def dp(i, k, z, left_in_a_row):
            if k == K:
                return 0

            res = 0
            if i < len(arr):
                res = dp(i+1, k+1, z, 0) + arr[i+1]
            
            if left_in_a_row < 2 and z < Z and i > 0:
                res = max(res, dp(i-1, k+1, z+1, left_in_a_row + 1) + arr[i-1])

            return res

        N, K, Z = map(int, input().split())
        arr = list(map(int, input().split()))
        print(dp(0, 0, 0, 0) + arr[0])

    for _ in range(int(input())):
        solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()