import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
group = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now, group_num):
    for next_node in graph[now]:
        if group[next_node] == 0:
            group[next_node] = group_num
            dfs(next_node, group_num)

cnt = 1

for i in range(1, n+1):
    if group[i] == 0:
        group[i] = cnt
        dfs(i, cnt)
        cnt += 1
        
print(group.count(1)-1)