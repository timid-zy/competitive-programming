import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    N, M = map(int, input().split())

    def find(x, parent):
        if x == parent[x]:
            return x

        parent[x] = find(parent[x], parent)
        return parent[x]

    def union(x, y, parent, size):
        r1, r2 = find(x, parent), find(y, parent)
        if r1 != r2:
            if size[r1] > size[r2]:
                parent[r2] = r1
                size[r1] += size[r2]
            else:
                parent[r1] = r2
                size[r2] += size[r1]
        

    parent = [i for i in range(N)]
    size = [1] * N
    for i in range(M):
        op, a, b = input().split()
        a, b = int(a) - 1, int(b) - 1

        if op == "union":
            union(a, b, parent, size)
        else:
            ans = "YES" if find(a, parent) == find(b, parent) else "NO"
            print(ans)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()