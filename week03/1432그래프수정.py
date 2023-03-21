import sys
import heapq
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
tmp = []

for _ in range(n):
    tmp.append(input().rstrip())
    
outorder = [0] * (n+1)
change = [0] * (n+1)

h = []

for i in range(n):
    for j in range(n):
        if tmp[i][j] == '1':
            graph[j+1].append(i+1)
            outorder[i+1] += 1
    if outorder[i+1] == 0:
        heapq.heappush(h, -(i+1))

num = n
while h:
    now = -heapq.heappop(h)
    change[now] = num
    num -= 1
    for next_node in graph[now]:
        outorder[next_node] -= 1
        if outorder[next_node] == 0:
            heapq.heappush(h, -next_node)

print(*change[1:]) if not 0 in change[1:] else print(-1)
        