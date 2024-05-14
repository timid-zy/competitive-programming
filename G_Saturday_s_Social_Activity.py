for i in range(int(input())):
    input()
    anatoli = list(map(int, input().split()))
    bisrat = list(map(int, input().split()))
    scores = [(i, anatoli[i] + bisrat[i] - 1) for i in range(len(anatoli))]
    def getScore(tup): return tup[1]
    scores.sort(key=getScore, reverse=True)
    turn = 0 # anatloi

    for i in range(len(scores)):
        idx, score = scores[i]
        if turn == 0:
            anatoli[idx] -= 1
            bisrat[idx] = 0
            turn = 1
        else:
            bisrat[idx] -= 1
            anatoli[idx] = 0
            turn = 0
    print(sum(anatoli) - sum(bisrat))