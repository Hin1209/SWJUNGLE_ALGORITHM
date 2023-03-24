import sys

input = sys.stdin.readline

n = int(input())

table = [0] * (n+1)
table[1] = 1
for i in range(2, n+1):
    table[i] = table[i-1] + table[i-2]

print(table[n])