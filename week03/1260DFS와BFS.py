import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for i in range(1, n+1):
    graph[i].sort()

def dfs(now):
        print(now, end=" ")
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = 1
                dfs(next_node)

def bfs(now):
    deq = deque()
    deq.append(now)
    visited[now] = 1
    while deq:
        now = deq.popleft()
        print(now, end=" ")
        for next_node in graph[now]:
            if not visited[next_node]:
                visited[next_node] = 1
                deq.append(next_node)

visited[v] = 1
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)