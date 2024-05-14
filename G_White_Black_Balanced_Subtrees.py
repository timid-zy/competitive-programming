import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        adj = [ [] for _ in range(n)]
        colors = input()

        for i in range(len(arr)):
            adj[arr[i] - 1].append(i + 1)
        
        
        def dfs(idx):
            nonlocal count
            
            white = black = 0
            for ed in adj[idx]:
                w, b = dfs(ed)
                white += w
                black += b
        
            if colors[idx] == "W":
                white += 1
            else:
                black += 1
            
            if white == black:
                count += 1

            return white, black

        count = 0
        dfs(0)
        print(count)
    
    pass
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
