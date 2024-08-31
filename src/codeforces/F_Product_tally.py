input()

arr = list(map(int, input().split()))
sign = [1] * len(arr)
sign[0] = 1 if arr[0] > 0 else -1


for i in range(1, len(arr)):
    if arr[i] < 0:
        sign[i] = sign[i - 1] * -1
    else:
        sign[i] = sign[i - 1]

pos = 1
neg = 0
pos_count = 0
neg_count = 0

for i in range(len(sign)):
    if sign[i] == 1:
        neg_count += neg
        pos_count += pos
        pos += 1

    elif sign[i] == -1:
        neg_count += pos
        pos_count += neg
        neg += 1

print(neg_count, pos_count)
