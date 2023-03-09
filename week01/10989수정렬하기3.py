import sys

input = sys.stdin.readline

n = int(input())
save = [0 for _ in range(10001)]

for i in range(n):
    save[int(input())] += 1

for i in range(len(save)):
    for j in range(save[i]):
        print(i)