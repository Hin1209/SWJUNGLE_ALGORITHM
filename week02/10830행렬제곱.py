import sys

input = sys.stdin.readline

MOD = 1000
n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

def matrix_mul(a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += (a[i][k] * b[k][j]) % MOD
            res[i][j] %= MOD
    return res

def matrix_pow(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= MOD
        return a
    half = b // 2
    res = matrix_pow(a, half)
    res = matrix_mul(res, res)
    if b % 2 == 1:
        res = matrix_mul(a, res)
    return res

ans = matrix_pow(matrix, b)
for i in ans:
    for j in i:
        print(j, end=" ")
    print()
    