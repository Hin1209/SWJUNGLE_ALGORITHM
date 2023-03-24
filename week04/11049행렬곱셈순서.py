import sys
input = sys.stdin.readline

n = int(input())

matrix = [tuple(map(int, input().split())) for _ in range(n)]
INF = int(1e9)

table = [[0] * n for _ in range(n)]

for i in range(1,n):
    for j in range(n-i):
        if i+j != j:
            table[j][j+i] = INF
        for k in range(j, j+i):
            compare = table[j][k] + table[k+1][j+i] + matrix[j][0]*matrix[k][1]*matrix[j+i][1]
            table[j][j+i] = min(table[j][j+i], compare)

print(table[0][n-1])