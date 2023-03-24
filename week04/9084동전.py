import sys

input = sys.stdin.readline

res = []
for _ in range(int(input())):

    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    
    table = [0] * (m+1)
    table[0] = 1
    
    for coin in coins:
        for i in range(coin, m+1):
            table[i] += table[i-coin]
    res.append(table[m])

for i in res:
    print(i)