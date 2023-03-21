import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
INF = 1e9
order = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    tall, small = map(int, input().split())
    graph[tall].append(small)
    order[small] += 1

result = []
deq = deque()
for i in range(1, n+1):
    if order[i] == 0:
        deq.append(i)

while deq:
    now = deq.popleft()
    result.append(now)
    for next in graph[now]:
        order[next] -= 1
        if order[next] == 0:
            deq.append(next)

for i in result:
    print(i, end = " ")