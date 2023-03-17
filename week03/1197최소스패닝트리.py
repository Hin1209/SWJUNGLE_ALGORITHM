import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())

edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
edges.sort()

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
parent = [0] * (v+1)

for i in range(v+1):
    parent[i] = i

result = 0
for c, a, b in edges:
    if find_parent(a, parent) != find_parent(b, parent):
        result += c
        union_parent(a, b, parent)
print(result)
