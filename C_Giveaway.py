n, k = list(map(int, input().split()))
prices = list(map(int, input().split()))
prices.sort()
prefix = [0]
for i in range(len(prices)): prefix.append(prefix[-1] + prices[i])

for i in range(k):
    x, y = list(map(int, input().split()))
    x = len(prefix) - x
    val = prefix[x - 1 + y] - prefix[x - 1]
    print(val)