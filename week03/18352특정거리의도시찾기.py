from collections import deque
import sys
n, m, k, x = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]
visited[x] = 0
for _ in range(m):
    index, next = list(map(int, sys.stdin.readline().split()))
    graph[index].append(next)

q = deque()
q.append(x)
result = []
while q:
    v = q.popleft()
    for nx in graph[v]:
        if visited[nx] == -1:
            q.append(nx)
            visited[nx] = visited[v] + 1
check = False
for i in range(len(visited)):
    if visited[i] == k:
        print(i)
        check = True
if not check:
    print(-1)



