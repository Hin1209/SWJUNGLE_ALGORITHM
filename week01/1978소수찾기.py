import sys

input = sys.stdin.readline


n = int(input())
save = list(map(int, input().split()))
cnt = 0

for i in range(len(save)):
    count = 0
    for j in range(1, save[i]):
        if save[i] % j == 0:
            count += 1
        if count >= 3:
            break
    if count == 1:
        cnt += 1

print(cnt)