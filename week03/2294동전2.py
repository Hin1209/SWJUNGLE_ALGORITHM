import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

INF = int(1e9)
price = [INF] * (k+1)
coin = []

deq = deque()
for _ in range(n):
    num = int(input())
    coin.append(num)
    deq.append((num,1))
    if num <= k:
        price[num] = 1 

while deq:
    cost, cnt = deq.popleft()
    if cost == k:
        break
    
    for add in coin:
        if cost + add <= k:
            if cnt + 1 < price[cost+add]:
                price[cost+add] = cnt + 1
                deq.append((cost+add, cnt+1))
    
print(price[k]) if price[k] < INF else print(-1)