import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)

small = [0] * (n+1)

for _ in range(m):
    small[int(input())] = 1
    
memo = {}

deq = deque()
deq.append((1, 0, 0))

min_jump = int(1e9)
while deq:
    now, cnt, jump = deq.popleft()
    
    if (now, jump) in memo:
        continue
    else:
        memo[(now, jump)] = cnt
        if now == n:
            min_jump = min(min_jump, cnt)
            continue
    
    if jump > 1:
        if now+jump-1 <= n and not small[now+jump-1]:
            deq.append((now+jump-1, cnt+1, jump-1))
    if jump > 0:
        if now+jump <= n and not small[now+jump]:
            deq.append((now+jump, cnt+1, jump))
    if now+jump+1 <= n and not small[now+jump+1]:
        deq.append((now+jump+1, cnt+1, jump+1))

print(min_jump) if min_jump < INF else print(-1)