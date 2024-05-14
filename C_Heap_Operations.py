from heapq import heappush, heappop

ans = []
heap = []
for __ in range(int(input())):

    command = list(input().split())
    if command[0] == "insert":
        heappush(heap, int(command[1]))
        ans.append(f"insert {int(command[1])}")
    
    elif command[0] == "removeMin":
        if len(heap) == 0:
            ans.append("insert 0")
            
        else:
            heappop(heap)
        
        ans.append("removeMin")
    
    else:
        while heap and int(command[1]) > heap[0]:
            x = heappop(heap)
            ans.append("removeMin")
        
        if not (heap and heap[0] == int(command[1])):
            heappush(heap, int(command[1]))
            ans.append(f"insert {int(command[1])}")
        
        ans.append(f"getMin {int(command[1])}")
    

print(len(ans))
for op in ans:
    print(op)