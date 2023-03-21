import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [{} for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
inorder = [0] * (n+1)
run = set()
dist = [-1] * (n+1)

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start][end] = cost
    inorder[end] += 1
    reverse_graph[end].append(start)
    
start, destination = map(int, input().split())

dist[start] = 0
deq = deque()
deq.append((start, 0))

while deq:
    now, cost = deq.popleft()
    for next_city in graph[now].keys():
        cost_road = graph[now][next_city]
        inorder[next_city] -= 1
        dist[next_city] = max(dist[next_city], cost + cost_road)
        if inorder[next_city] == 0:
            deq.append((next_city, dist[next_city]))
 
deq.append(destination)
visited = [0] * (n+1)
visited[destination] = 1
total_road = set()
while deq:
    now = deq.popleft()
    for next_city in reverse_graph[now]:
        cost = graph[next_city][now]
        if dist[next_city] + cost == dist[now]:
            total_road.add((next_city, now))
            if not visited[next_city]:
                deq.append(next_city)
                visited[next_city] = 1
print(dist[destination])
print(len(total_road))
