L, D, K = map(int, input().split())

lane = ((K - 1) // (D * 2)) + 1

last = (K // (D * 2)) * (D * 2)
if last == K:
    last -= D*2

# print(last)
desk = ((K - last - 1) // 2) + 1
side = "L" if K % 2 == 1 else "R"

print(lane, desk, side)