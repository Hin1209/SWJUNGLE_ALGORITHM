import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

inorder = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    inorder[x] += 1

fundamental = [{} for _ in range(n+1)]
deq = deque()
for i in range(1, n+1):
    if inorder[i] == 0:
        deq.append(i)
        fundamental[i][i] = 1

while deq:
    node = deq.popleft()
    for next_node, cnt in graph[node]:
        for key in fundamental[node].keys():
            if key in fundamental[next_node]:
                fundamental[next_node][key] += cnt * fundamental[node][key]
            else:
                fundamental[next_node][key] = cnt * fundamental[node][key]
        inorder[next_node] -= 1
        if inorder[next_node] == 0:
            deq.append(next_node)

result = [] 
for key in fundamental[n].keys():
    result.append((key, fundamental[n][key]))

result.sort()
for num, cnt in result:
    print(num, cnt)