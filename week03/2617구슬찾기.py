import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
num_heavy = [0] * (n+1)
inorder_heavy = [0] * (n+1)
num_light = [0] * (n+1)
inorder_light = [0] * (n+1)

for _ in range(m):
    heavy, light = map(int, input().split())
    graph[heavy].append(light)
    inorder_heavy[light] += 1
    reverse_graph[light].append(heavy)
    inorder_light[heavy] += 1
    
heavy_deq = deque()
light_deq = deque()

res = 0
for i in range(1, n+1):
    light_deq.append(i)
    cnt_light = 0
    visited = [0] * (n+1)
    visited[i] = 1
    while light_deq:
        node = light_deq.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                cnt_light += 1
                light_deq.append(next_node)
    visited = [0] * (n+1)
    visited[i] = 1
    heavy_deq.append(i)
    cnt_heavy = 0
    while heavy_deq:
        node = heavy_deq.popleft()
        for next_node in reverse_graph[node]:
            if not visited[next_node]:
                visited[next_node] = 1
                cnt_heavy += 1
                heavy_deq.append(next_node)
    if cnt_heavy >= (n+1) // 2 or cnt_light >= (n+1) // 2:
        res += 1
    
print(res)