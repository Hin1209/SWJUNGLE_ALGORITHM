import sys
input = sys.stdin.readline

n, k = map(int, input().split())

bag = [tuple(map(int, input().split())) for _ in range(n)]

bag.sort()

table = [[0] * n for _ in range(k+1)]

for idx in range(n):
    weight = bag[idx][0]
    value = bag[idx][1]
    for i in range(k+1):
        if i < weight:
            table[i][idx] = table[i][idx-1] if idx > 0 else 0
        else:
            table[i][idx] = max(table[i][idx-1], table[i-weight][idx-1]+value) if idx > 0 else value

print(max(table[k]))