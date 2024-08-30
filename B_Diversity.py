word = input()
target = int(input())
chrs = set()
for c in word:
    chrs.add(c)

ans = max(target - len(chrs), 0) if len(word) >= target else "impossible"
print(ans)