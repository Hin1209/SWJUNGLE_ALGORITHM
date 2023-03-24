import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
    
price = k
cnt = 0
idx = 0

while price > 0:
    if price // coins[idx] != 0:
        cnt += price // coins[idx]
        price = price % coins[idx]
    idx += 1

print(cnt)