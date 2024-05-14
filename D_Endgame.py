import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, k, A, B = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    avengers = {}
    for i in range(len(arr)):
        avengers[arr[i]] = avengers.get(arr[i], 0) + 1

    def rec(start, end):
        if start >= end:
            if start in avengers:
                return B, 1
            else:
                return A, 0
        
        if start == end + 1:
            if start in avengers and end in avengers:
                return B * 4, 2
            elif start in avengers or end in avengers:
                return B, 1
            else:
                return A, 0

        mid = (end + start) // 2
        left_p, left_count = rec(start, mid)
        right_p, right_count = rec(mid + 1, end)
        
        curr_p = B * (left_count + right_count) * (end - start + 1)
        # contains no avengers
        if left_count + right_count == 0:
            curr_p = A

        return min(left_p + right_p, curr_p), left_count + right_count

    print(rec(1, pow(2, n))[0])
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()