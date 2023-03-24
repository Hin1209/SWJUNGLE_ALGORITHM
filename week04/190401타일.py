import sys

input = sys.stdin.readline

n = int(input())

table = [0] * 1000001

MOD = 15746

table[1] = 1
table[2] = 2

for i in range(3, n+1):
    table[i] = (table[i-1] + table[i-2]) % MOD
print(table[n])