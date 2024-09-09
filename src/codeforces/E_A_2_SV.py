import sys, threading
from collections import defaultdict
input = lambda: sys.stdin.readline().strip()

def main():
    def solve():
        def dfs(node):
            if node == 1:
                res = []
                for nb in graph[node]:
                    children = dfs(nb)
                    sx = sy = 0
                    for c in children:
                        sx += c[0]; sy += c[1]
                    
                    res.append((sx, sy))
                
                return res

            for nb in graph[node]:
                
        
        graph = defaultdict(list)
        N = int(input())
        A = list(map(int, input().split()))
        for i in range(A):
            graph[A[i]].append(i+1)
        
        children = dfs(1)

    for _ in range(int(input())):
        print(solve())
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()