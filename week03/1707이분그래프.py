import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [0] * (v+1)

    can_divided = True
    for i in range(1, v+1):
        if not visited[i]:
            deq = deque()
            deq.append(i)
            visited[i] = 1
            while deq:
                now = deq.popleft()
                for next_node in graph[now]:
                    if not visited[next_node]:
                        visited[next_node] = -visited[now]
                        deq.append(next_node)
                    elif visited[next_node] == visited[now]:
                        can_divided = False
    
    if can_divided:
        print("YES")
    else:
        print("NO")