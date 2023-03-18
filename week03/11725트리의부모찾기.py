import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
parent = [0] * (n+1)
parent[1] = 1

deq = deque()
deq.append(1)

while deq:
    now = deq.popleft()
    for next_node in graph[now]:
        if parent[next_node] != 0:
            continue
        parent[next_node] = now
        deq.append(next_node)
    
for i in range(2, n+1):
    print(parent[i])