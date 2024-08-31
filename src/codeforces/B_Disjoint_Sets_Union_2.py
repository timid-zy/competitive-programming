import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        r1, r2 = find(x), find(y)
        if r1 != r2:
            if size[r1] > size[r2]:
                parent[r2] = r1
                size[r1] += size[r2]
                mn[r1] = min(mn[r1], mn[r2])
                mx[r1] = max(mx[r1], mx[r2])
            
            else:
                parent[r1] = r2
                size[r2] += size[r1]
                mn[r2] = min(mn[r1], mn[r2])
                mx[r2] = max(mx[r1], mx[r2])

    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    size = [1] * N
    mn = [i for i in range(N)]
    mx = [i for i in range(N)]
    
    for _ in range(M):
        op = input().split()

        if op[0] == "union":
            union(int(op[1]) - 1, int(op[2]) - 1)
        else:
            p = find(int(op[1]) - 1)
            print(mn[p] + 1, mx[p] + 1, size[p])
  
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()