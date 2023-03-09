t = int(input())
for _ in range(t):
    score = 0
    cnt = 0
    st = input()
    for i in range(len(st)):
        if st[i] == "O":
            cnt += 1
        elif st[i] == "X" and cnt != 0:
            score += int(cnt * (cnt + 1) / 2)
            cnt = 0
        if st[i] == "O" and i == len(st) - 1:
            score += int(cnt * (cnt + 1) / 2)
    print(score)