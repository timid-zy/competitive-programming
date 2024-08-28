from collections import deque

for _ in range(int(input())):
    def bfs(target):
        queue = deque([[0]])
        ans = None
        while queue:
            curr = queue.popleft()
            sum_ = sum(curr)
            if sum_ == target:
                ans = curr
                break
                
            if sum_ > target:
                continue
                
            for n in range(curr[-1] + 1, 10):
                queue.append(curr + [n])
        
        return "".join(map(str, ans))[1:]

    print(bfs(int(input())))
