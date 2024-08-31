from collections import defaultdict, deque
# import sys, threading

# input = lambda: sys.stdin.readline().strip()

# def main():
#     def solve():
#         def dfs(node):
#             if len(graph[node]) == 0:
#                 return V[node-1]
            
#             children = float('inf')
#             for nb in graph[node]:
#                 children = min(children, dfs(nb))
        
#             if node == 1:
#                 return children + V[0]
            
#             if V[node-1] >= children:
#                 return children

#             return V[node-1] + ((children - V[node-1]) // 2)

#         input()
#         V = list(map(int, input().split()))
#         P = list(map(int, input().split()))
#         graph = defaultdict(list)
#         for i in range(len(P)):
#             graph[P[i]].append(i+2)
        
#         return dfs(1)
    
#     for _ in range(int(input())):
#         print(solve())
    
# if __name__ == '__main__':
    
#     sys.setrecursionlimit(1 << 30)
#     threading.stack_size(1 << 27)

#     main_thread = threading.Thread(target=main)
#     main_thread.start()
#     main_thread.join()

def solve():
    input()
    V = list(map(int, input().split()))
    P = list(map(int, input().split()))
    graph = defaultdict(list)
    indeg = defaultdict(int)
    for i in range(len(P)):
        graph[P[i]].append(i+2)
        indeg[P[i]] += 1

    vals = [float('inf') for _ in range(len(V))]
    queue = deque()
    for i in range(1, len(V) + 1):
        if indeg[i] == 0:
            queue.append(i)

    while queue:
        curr = queue.popleft()
        if len(graph[curr]) == 0:
            vals[curr-1] = V[curr-1]
        else:
            children = float('inf')
            for nb in graph[curr]:
                children = min(children, vals[nb-1])
        
            if curr == 1:
                vals[curr-1] =  children + V[0]
            elif V[curr-1] >= children:
                vals[curr-1] = children
            else:
                vals[curr-1] = V[curr-1] + ((children - V[curr-1]) // 2)
            
        if curr == 1:
            continue

        indeg[P[curr-2]] -= 1
        if indeg[P[curr-2]] == 0:
            queue.append(P[curr-2])

    return vals[0]

for _ in range(int(input())):
    print(solve())