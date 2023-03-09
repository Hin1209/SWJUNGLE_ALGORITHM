import sys

input = sys.stdin.readline

c = int(input())

for _ in range(c):
    scores = list(map(int, input().split()))
    cnt = scores[0]
    avg = sum(scores[1:]) / cnt
    over_avg = 0
    for i in range(1, cnt+1):
        if scores[i] > avg:
            over_avg += 1
    print("{:.3f}%".format(over_avg / cnt * 100))