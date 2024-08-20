a, b, c, d = map(int, input().split())

misha = max(3 * a / 10, a - (a / 250 * c))
vasya = max(3 * b / 10, b - (b / 250 * d))

ans = "Misha" if misha > vasya else "Vasya" if vasya > misha else "Tie"
print(ans)