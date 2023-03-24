import sys
input = sys.stdin.readline

n = int(input())

world = [] 
for i in range(n):
    world.append(list(map(int, input().split())))

INF = 1e9
memo = {}

for i in range(n):
    for j in range(n):
        if world[i][j] == 0:
            world[i][j] = INF

def find_min(now, visited):
    if visited == (1 << n) - 1:
        return world[now][0]
    
    if (now, visited) in memo:
        return memo[(now, visited)]
    
    min_cost = INF
    
    for i in range(1,n):
        if not(visited & (1 << i)):
            cost = find_min(i, visited | (1 << i)) + world[now][i]
            min_cost = min(min_cost, cost)
    memo[(now, visited)] = min_cost
    return min_cost

print(find_min(0,1))
